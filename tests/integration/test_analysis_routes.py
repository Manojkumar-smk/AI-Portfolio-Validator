import pytest
import json

def test_github_deep_check_valid(client):
    """Test the GitHub deep check endpoint with a valid URL."""
    payload = {"github_url": "https://github.com/testuser"}
    response = client.post('/api/analysis/github-deep-check', json=payload)
    
    assert response.status_code == 200
    data = response.get_json()
    assert data["username"] == "testuser"
    assert "originality_check" in data

def test_github_deep_check_missing_url(client):
    """Test the GitHub deep check endpoint with missing URL."""
    payload = {}
    response = client.post('/api/analysis/github-deep-check', json=payload)
    
    assert response.status_code == 400
    assert "error" in response.get_json()

def test_compare_candidates_valid(client):
    """Test the compare candidates endpoint."""
    payload = {"candidate_ids": ["id1", "id2"]}
    response = client.post('/api/analysis/compare', json=payload)
    
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2

def test_compare_candidates_empty(client):
    """Test the compare candidates endpoint with empty list."""
    payload = {"candidate_ids": []}
    response = client.post('/api/analysis/compare', json=payload)
    
    assert response.status_code == 400
    assert "error" in response.get_json()
