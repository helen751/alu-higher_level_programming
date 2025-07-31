#!/usr/bin/python3
"""__summary__
- writes a script that takes in a URL as a command line argument
- sends a request to the URL
- and displays the value
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
