#!/usr/bin/python3
"""POST a letter as q to an API and display results"""
import requests
import sys

q = ""
if len(sys.argv) > 1:
    q = sys.argv[1]
r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})

try:
    result = r.json()
    if result:
        print("[{}] {}".format(result.get("id"), result.get("name")))
    else:
        print("No result")
except Exception:
    print("Not a valid JSON")
