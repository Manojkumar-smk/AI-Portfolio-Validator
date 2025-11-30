from app.services.github_scanner import github_scanner
import json

def debug_repo_analysis(username):
    print(f"--- Detailed Repository Analysis for {username} ---\n")
    
    print("Fetching repositories...")
    repos = github_scanner.get_user_repos(username)
    print(f"Found {len(repos)} repositories.\n")
    
    for i, repo in enumerate(repos):
        print(f"[{i+1}] {repo['name']}")
        print(f"    Description: {repo.get('description', 'N/A')}")
        print(f"    Stars: {repo.get('stargazers_count', 0)} | Forks: {repo.get('forks_count', 0)}")
        print(f"    Open Issues: {repo.get('open_issues_count', 0)}")
        print(f"    Topics: {repo.get('topics', [])}")
        print(f"    Created: {repo.get('created_at')} | Updated: {repo.get('updated_at')}")
        
        # Fetch languages
        print("    Fetching languages...")
        langs = github_scanner.get_repo_languages(username, repo['name'])
        print(f"    Languages: {json.dumps(langs)}")
        print("-" * 60)

if __name__ == "__main__":
    debug_repo_analysis("Manojkumar-smk")
