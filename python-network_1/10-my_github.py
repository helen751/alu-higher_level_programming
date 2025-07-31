#!/usr/bin/python3
"""Uses GitHub API to display your id"""
import requests
import sys

username = sys.argv[1]
token = sys.argv[2]
url = "https://api.github.com/user"
r = requests.get(url, auth=(username, token))
try:
    print(r.json().get("id"))
except Exception:
    print(None)
