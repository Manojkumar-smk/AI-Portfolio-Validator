import requests
import os
from reportlab.pdfgen import canvas

BASE_URL = "http://127.0.0.1:5000/api"

def create_dummy_pdf(filename="dummy_resume.pdf"):
    """Creates a simple PDF file for testing."""
    c = canvas.Canvas(filename)
    c.drawString(100, 750, "John Doe")
    c.drawString(100, 730, "Email: john.doe@example.com")
    c.drawString(100, 710, "GitHub: https://github.com/johndoe")
    c.drawString(100, 690, "Skills: Python, Flask, React, SQL, Docker")
    c.drawString(100, 670, "Experience: Senior Python Developer with 5 years of experience.")
    c.save()
    print(f"Created dummy PDF: {filename}")
    return filename

def test_api_flow():
    print("Starting API Integration Test...\n")

    # 1. Create a Job
    print("1. Creating a Job...")
    job_payload = {
        "title": "Senior Python Engineer",
        "description": "We are looking for a Python expert with Flask, React, and SQL skills. Docker experience is a plus.",
        "requirements": "5+ years experience"
    }
    try:
        resp = requests.post(f"{BASE_URL}/jobs/", json=job_payload)
        resp.raise_for_status()
        job_data = resp.json().get("data", [])
        if isinstance(job_data, list) and len(job_data) > 0:
            job_id = job_data[0].get("id")
        else:
            job_id = job_data.get("id")
        print(f"   Success! Job ID: {job_id}")
    except Exception as e:
        print(f"   Failed to create job: {e}")
        return

    # 2. Create a Candidate (with Resume Upload)
    print("\n2. Creating a Candidate with Resume...")
    pdf_file = create_dummy_pdf()
    
    try:
        with open(pdf_file, 'rb') as f:
            files = {'resume': (pdf_file, f, 'application/pdf')}
            data = {
                'name': 'John Doe',
                'email': 'john.doe@example.com',
                'github_url': 'https://github.com/johndoe'
            }
            resp = requests.post(f"{BASE_URL}/candidates/", data=data, files=files)
            resp.raise_for_status()
            candidate_data = resp.json().get("data", {})
            # Handle case where data might be a list or dict depending on Supabase return
            if isinstance(candidate_data, list) and len(candidate_data) > 0:
                candidate_id = candidate_data[0].get("id")
            else:
                candidate_id = candidate_data.get("id")
                
            print(f"   Success! Candidate ID: {candidate_id}")
    except Exception as e:
        print(f"   Failed to create candidate: {e}")
        return
    finally:
        if os.path.exists(pdf_file):
            os.remove(pdf_file)

    # 3. Evaluate Candidate
    print(f"\n3. Evaluating Candidate {candidate_id} against Job {job_id}...")
    eval_payload = {
        "job_id": job_id
    }
    try:
        resp = requests.post(f"{BASE_URL}/analysis/evaluate/{candidate_id}", json=eval_payload)
        resp.raise_for_status()
        report = resp.json()
        print("   Success! Evaluation Report:")
        print(f"   - Authenticity Score: {report.get('authenticity_score')}")
        print(f"   - Skill Match Score: {report.get('skill_match_score')}")
        print(f"   - Overall Score: {report.get('overall_score')}")
    except Exception as e:
        print(f"   Failed to evaluate candidate: {e}")

    # 4. Compare Candidates
    print(f"\n4. Comparing Candidates [ID: {candidate_id}]...")
    compare_payload = {
        "candidate_ids": [candidate_id]
    }
    try:
        resp = requests.post(f"{BASE_URL}/analysis/compare", json=compare_payload)
        resp.raise_for_status()
        comparison_results = resp.json()
        print("   Success! Comparison Results:")
        for res in comparison_results:
            print(f"   - Candidate {res.get('candidate_id')}: Score {res.get('overall_score')}")
    except Exception as e:
        print(f"   Failed to compare candidates: {e}")

    print("\nTest Complete.")

if __name__ == "__main__":
    test_api_flow()
