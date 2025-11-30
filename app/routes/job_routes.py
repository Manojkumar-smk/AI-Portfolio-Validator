from flask import Blueprint, request, jsonify
from app.services.supabase_client import supabase

job_bp = Blueprint('job', __name__, url_prefix='/api/jobs')

@job_bp.route('/', methods=['POST'])
def create_job():
    """
    Creates a new job description.
    """
    data = request.json
    if not data or not data.get('title'):
        return jsonify({"error": "Title is required"}), 400

    job_data = {
        "title": data.get("title"),
        "description": data.get("description"),
        "requirements": data.get("requirements") # Optional structured requirements
    }

    if supabase:
        try:
            response = supabase.table("jobs").insert(job_data).execute()
            return jsonify({"message": "Job created", "data": response.data}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"message": "Supabase not configured", "data": job_data}), 201

@job_bp.route('/', methods=['GET'])
def list_jobs():
    if supabase:
        try:
            response = supabase.table("jobs").select("*").execute()
            return jsonify(response.data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify([]), 200
