#!/usr/bin/python3
import requests
import sys

def fetch_recent_commits(repository_name, owner_name):
    """Fetches and prints the 10 most recent commits of a repository."""
    url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            commits = response.json()

            for commit in commits[:10]:
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    fetch_recent_commits(repo_name, owner_name)
