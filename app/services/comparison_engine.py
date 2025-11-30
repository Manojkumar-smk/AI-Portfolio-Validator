class ComparisonEngine:
    def compare_candidates(self, candidate_ids):
        """
        Compares multiple candidates based on their evaluation reports.
        """
        # Fetch evaluations from DB (Mocking this part as we don't have the DB layer fully wired in this snippet)
        results = []
        for cid in candidate_ids:
            # Mock fetching data
            results.append({
                "candidate_id": cid,
                "name": f"Candidate {cid}",
                "overall_score": 85 + (hash(str(cid)) % 10) # Simple mock score variation
            })
        
        # Sort by score
        results.sort(key=lambda x: x['overall_score'], reverse=True)
        return results

comparison_engine = ComparisonEngine()
