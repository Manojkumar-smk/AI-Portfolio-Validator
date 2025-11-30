from app.services.github_scanner import github_scanner
import json

def fetch_all_data(username):
    print(f"--- RAW DATA DUMP FOR {username} ---\n")

    # 1. User Profile
    print(">>> USER PROFILE (GET /users/{username})")
    profile = github_scanner.get_user_profile(username)
    print(json.dumps(profile, indent=2))
    print("\n" + "="*50 + "\n")

    # 2. Repositories (Sample of first one)
    print(">>> REPOSITORY SAMPLE (GET /users/{username}/repos [0])")
    repos = github_scanner.get_user_repos(username)
    if repos:
        print(f"Total Repos Found: {len(repos)}")
        print("Sample Data from first repo:")
        print(json.dumps(repos[0], indent=2))
        
        # 4. Languages for this repo
        print("\n>>> LANGUAGES SAMPLE (GET /repos/{owner}/{repo}/languages)")
        langs = github_scanner.get_repo_languages(username, repos[0]['name'])
        print(json.dumps(langs, indent=2))
    else:
        print("No repositories found.")
    print("\n" + "="*50 + "\n")

    # 3. Events (Sample of first one)
    print(">>> EVENT SAMPLE (GET /users/{username}/events [0])")
    events = github_scanner.get_user_events(username)
    if events:
        print(f"Total Events Found: {len(events)}")
        print("Sample Data from first event:")
        print(json.dumps(events[0], indent=2))
    else:
        print("No events found.")
    print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    fetch_all_data("Manojkumar-smk")
