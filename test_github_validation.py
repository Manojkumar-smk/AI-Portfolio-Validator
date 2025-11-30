from app import create_app
import json

def test_github_deep_check():
    app = create_app()
    client = app.test_client()

    print("Testing GitHub Deep Validations API...")

    # Test Case 1: Valid GitHub URL
    payload = {"github_url": "https://github.com/Manojkumar-smk"}
    print(f"\nTest Case 1: Valid URL {payload}")
    response = client.post('/api/analysis/github-deep-check', json=payload)
    
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Response:")
        print(json.dumps(response.json, indent=2))
    else:
        print("Error:", response.json)

    # Test Case 2: Missing GitHub URL
    payload = {}
    print(f"\nTest Case 2: Missing URL {payload}")
    response = client.post('/api/analysis/github-deep-check', json=payload)
    
    print(f"Status Code: {response.status_code}")
    print("Response:", response.json)

if __name__ == "__main__":
    test_github_deep_check()
