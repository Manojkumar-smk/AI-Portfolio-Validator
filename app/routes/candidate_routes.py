from flask import Blueprint, request, jsonify
from app.services.resume_parser import resume_parser
from app.services.supabase_client import supabase

candidate_bp = Blueprint('candidate', __name__, url_prefix='/api/candidates')

@candidate_bp.route('/', methods=['POST'])
def create_candidate():
    """
    Creates a new candidate. 
    Expects JSON with 'name', 'email', etc. OR a file upload (multipart/form-data).
    """
    data = request.form.to_dict() if request.form else request.json
    file = request.files.get('resume')
    
    resume_text = ""
    parsed_details = {}

    if file:
        # Read file into memory and parse
        resume_text = resume_parser.extract_text(file)
        parsed_details = resume_parser.parse_details(resume_text)
    
    candidate_data = {
        "name": data.get("name", "Unknown"),
        "email": data.get("email") or parsed_details.get("email"),
        "linkedin_url": data.get("linkedin_url") or parsed_details.get("linkedin_url"),
        "github_url": data.get("github_url") or parsed_details.get("github"),
        "resume_text": resume_text
    }

    # Insert into Supabase
    if supabase:
        try:
            response = supabase.table("candidates").insert(candidate_data).execute()
            return jsonify({"message": "Candidate created", "data": response.data}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"message": "Supabase not configured", "data": candidate_data}), 201

@candidate_bp.route('/', methods=['GET'])
def list_candidates():
    """
    Lists all candidates.
    """
    if supabase:
        try:
            response = supabase.table("candidates").select("*").execute()
            return jsonify(response.data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify([]), 200
