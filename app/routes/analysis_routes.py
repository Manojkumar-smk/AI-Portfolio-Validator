from flask import Blueprint, request, jsonify
from app.services.ai_analyzer import ai_analyzer
from app.services.supabase_client import supabase

analysis_bp = Blueprint('analysis', __name__, url_prefix='/api/analysis')

@analysis_bp.route('/evaluate/<candidate_id>', methods=['POST'])
def evaluate_candidate(candidate_id):
    """
    Triggers evaluation for a specific candidate.
    Optional: Pass job_description_id in body.
    """
    # 1. Fetch candidate from DB
    candidate_data = {}
    if supabase:
        try:
            response = supabase.table("candidates").select("*").eq("id", candidate_id).execute()
            if not response.data:
                return jsonify({"error": "Candidate not found"}), 404
            candidate_data = response.data[0]
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        # Mock data if DB not ready
        candidate_data = {"id": candidate_id, "github_url": "https://github.com/torvalds"}

    # 2. Fetch Job Description (if provided)
    job_description = None
    data = request.json or {}
    job_id = data.get('job_id')
    
    if job_id and supabase:
        try:
            job_res = supabase.table("jobs").select("description").eq("id", job_id).execute()
            if job_res.data:
                job_description = job_res.data[0]['description']
        except Exception as e:
            print(f"Error fetching job: {e}")

    # 3. Perform Analysis
    report = ai_analyzer.analyze_candidate(candidate_data, job_description)

    # 3. Store Result in DB
    if supabase:
        try:
            eval_data = {
                "candidate_id": candidate_id,
                "authenticity_score": report['authenticity_score'],
                "skill_match_score": report['skill_match_score'],
                "overall_score": report['overall_score'],
                "detailed_report": report
            }
            supabase.table("evaluations").insert(eval_data).execute()
        except Exception as e:
            print(f"Error saving evaluation: {e}")

    return jsonify(report), 200

@analysis_bp.route('/compare', methods=['POST'])
def compare_candidates():
    from app.services.comparison_engine import comparison_engine
    data = request.json
    candidate_ids = data.get('candidate_ids', [])
    
    if not candidate_ids:
        return jsonify({"error": "No candidate_ids provided"}), 400

    comparison = comparison_engine.compare_candidates(candidate_ids)
    return jsonify(comparison), 200
