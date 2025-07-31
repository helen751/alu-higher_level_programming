#!/usr/bin/python3
#!/usr/bin/python3
"""__summary__
- writes a script that takes in a GitHub username and password
- uses the GitHub API to display the user's ID
- authenticating with the provided credentials
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    auth = (username, password)

    reqs = requests.get(url, auth=auth)
    print(reqs.json().get("id"))
