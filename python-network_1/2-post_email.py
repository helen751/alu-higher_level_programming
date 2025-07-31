#!/usr/bin/python3
"""__summary__
- Write a Python script takes in a URL
- and an email address
- with a letter as a parameter
- and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
