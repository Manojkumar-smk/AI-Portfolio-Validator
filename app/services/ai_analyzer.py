from app.services.github_scanner import github_scanner
from app.services.resume_parser import resume_parser

class AIAnalyzer:
    def analyze_candidate(self, candidate_data, job_description=None):
        """
        Orchestrates the analysis process:
        1. Fetch GitHub data
        2. Analyze authenticity
        3. Match skills with JD (if provided)
        4. Generate report
        """
        github_url = candidate_data.get('github_url')
        username = self._extract_username(github_url)
        
        github_data = {}
        if username:
            github_data['profile'] = github_scanner.get_user_profile(username)
            github_data['repos'] = github_scanner.get_user_repos(username)

        # Mock AI Analysis Logic
        authenticity_score = self._calculate_authenticity(github_data)
        skill_match_score = self._calculate_skill_match(candidate_data, job_description)
        
        report = {
            "authenticity_score": authenticity_score,
            "skill_match_score": skill_match_score,
            "overall_score": (authenticity_score + skill_match_score) / 2,
            "summary": "Candidate shows strong potential based on GitHub activity.",
            "strengths": ["Consistent commit history", "Python expertise"],
            "red_flags": [],
            "github_analysis": github_data # simplified for storage
        }
        
        return report

    def _extract_username(self, github_url):
        if not github_url:
            return None
        return github_url.rstrip('/').split('/')[-1]

    def _calculate_authenticity(self, github_data):
        # Use GitHubValidator for real authenticity check
        if not github_data.get('profile'):
            return 0
            
        from app.services.github_validator import github_validator
        
        # We can reconstruct the URL or just pass the username if we modify validator, 
        # but validator takes URL. Let's use the profile URL.
        profile_url = github_data['profile'].get('html_url')
        if not profile_url:
            return 50
            
        validation = github_validator.validate_github_profile(profile_url)
        risk_score = validation.get('overall_risk_score', 50)
        
        # Authenticity is inverse of Risk
        return 100 - risk_score

    def _calculate_skill_match(self, candidate_data, job_description):
        if not job_description:
            return 0
            
        resume_text = candidate_data.get('resume_text', '').lower()
        jd_text = job_description.lower()
        
        # Very basic keyword matching for demonstration
        # In a real app, use an LLM or embeddings here
        keywords = ['python', 'flask', 'react', 'sql', 'api', 'docker', 'aws']
        
        jd_keywords = [kw for kw in keywords if kw in jd_text]
        if not jd_keywords:
            return 50 # Neutral score if no known keywords found in JD
            
        matched_keywords = [kw for kw in jd_keywords if kw in resume_text]
        
        score = (len(matched_keywords) / len(jd_keywords)) * 100
        return round(min(score, 100), 2)

ai_analyzer = AIAnalyzer()
