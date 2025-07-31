#!/usr/bin/python3
"""Lists 10 commits (sha & author) of a repo by user via GitHub API"""
import requests
import sys

repo = sys.argv[1]
owner = sys.argv[2]
url = f"https://api.github.com/repos/{owner}/{repo}/commits"
r = requests.get(url)
try:
    commits = r.json()
    for commit in commits[:10]:
        sha = commit.get("sha")
        author = commit.get("commit", {}).get("author", {}).get("name")
        print(f"{sha}: {author}")
except Exception:
    pass
