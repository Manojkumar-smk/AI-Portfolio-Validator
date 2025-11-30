import pytest
from app.services.github_validator import github_validator

def test_validate_github_profile_valid_url():
    """Test validation with a valid GitHub URL."""
    url = "https://github.com/testuser"
    result = github_validator.validate_github_profile(url)
    
    assert result["username"] == "testuser"
    assert "originality_check" in result
    assert "commit_pattern_authenticity" in result
    assert "overall_risk_score" in result
    assert isinstance(result["overall_risk_score"], int)

def test_validate_github_profile_invalid_url():
    """Test validation with an invalid/empty URL."""
    result = github_validator.validate_github_profile("")
    assert result == None or "error" in result # Depending on implementation

def test_extract_username():
    """Test username extraction logic."""
    assert github_validator._extract_username("https://github.com/user") == "user"
    assert github_validator._extract_username("https://github.com/user/") == "user"
    assert github_validator._extract_username(None) is None
