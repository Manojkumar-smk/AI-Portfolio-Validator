import requests
import json

BASE_URL = "http://127.0.0.1:5000/api/analysis"

def test_evaluate_candidate(candidate_id, name, email, github_url, resume_text):
    print(f"\n--- Testing Evaluation for {name} (ID: {candidate_id}) ---")
    
    create_url = "http://127.0.0.1:5000/api/candidates/"
    candidate_payload = {
        "name": name,
        "email": email,
        "github_url": github_url,
        "resume_text": resume_text
    }
    
    print("1. Creating Candidate...")
    try:
        create_res = requests.post(create_url, json=candidate_payload)
        if create_res.status_code in [200, 201]:
            print("   Candidate created successfully.")
            data = create_res.json().get('data')
            if data and isinstance(data, list) and len(data) > 0:
                candidate_id = data[0]['id']
            elif data and isinstance(data, dict):
                 candidate_id = data.get('id', candidate_id)
            print(f"   Using ID: {candidate_id}")
        else:
            print(f"   Failed to create candidate: {create_res.text}")
    except Exception as e:
        print(f"   Error creating candidate: {e}")

    print(f"2. Evaluating Candidate ID: {candidate_id}...")
    evaluate_url = f"{BASE_URL}/evaluate/{candidate_id}"
    
    try:
        res = requests.post(evaluate_url, json={"job_id": "dummy_job_id"})
        print(f"Status Code: {res.status_code}")
        try:
            print(json.dumps(res.json(), indent=2))
        except:
            print(res.text)
    except Exception as e:
        print(f"Error evaluating: {e}")

if __name__ == "__main__":
    akilan_resume = "Akilan Kumar S\nEmbedded Engineer..."
    manoj_resume = "Manojkumar. S\nSAP Techno-functional Consultant..."

    test_evaluate_candidate("7", "Akilan Kumar S", "akilan6793eee@gmail.com", "https://github.com/akilan6793eee/", akilan_resume)
    test_evaluate_candidate("9", "Manojkumar.smk", "manojkumar.smk09@gmail.com", "https://github.com/Manojkumar-smk", manoj_resume)
