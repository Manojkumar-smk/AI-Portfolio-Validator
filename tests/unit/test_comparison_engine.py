import pytest
from app.services.comparison_engine import comparison_engine

def test_compare_candidates_string_ids():
    """Test that comparison engine handles string IDs correctly."""
    candidate_ids = ["uuid-1", "uuid-2", "uuid-3"]
    results = comparison_engine.compare_candidates(candidate_ids)
    
    assert len(results) == 3
    assert results[0]['overall_score'] >= results[1]['overall_score']
    assert isinstance(results[0]['overall_score'], int)

def test_compare_candidates_empty_list():
    """Test that comparison engine handles empty list."""
    results = comparison_engine.compare_candidates([])
    assert results == []

def test_compare_candidates_structure():
    """Test the structure of the returned results."""
    candidate_ids = ["test-id"]
    results = comparison_engine.compare_candidates(candidate_ids)
    
    assert len(results) == 1
    item = results[0]
    assert "candidate_id" in item
    assert "name" in item
    assert "overall_score" in item
    assert item["candidate_id"] == "test-id"
