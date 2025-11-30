from app.services.comparison_engine import comparison_engine
import json

def test_comparison():
    print("Testing Comparison Engine...")
    
    # Test case 1: String IDs (UUIDs)
    ids_1 = ["uuid-1", "uuid-2", "uuid-3"]
    print(f"\nTest Case 1: String IDs {ids_1}")
    results_1 = comparison_engine.compare_candidates(ids_1)
    print(json.dumps(results_1, indent=2))

    # Test case 2: Mixed IDs (just in case)
    ids_2 = ["user-A", "user-B"]
    print(f"\nTest Case 2: More String IDs {ids_2}")
    results_2 = comparison_engine.compare_candidates(ids_2)
    print(json.dumps(results_2, indent=2))

if __name__ == "__main__":
    test_comparison()
