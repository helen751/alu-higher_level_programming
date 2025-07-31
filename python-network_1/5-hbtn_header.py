#!/usr/bin/python3
"""__summary__
- Write a Python script that takes in a URL
- and displays the value of the X-Request-Id variable found in the header of the
- response.
"""
import sys
import requests

if __name__ == '__main__':
    reqs = requests.get(sys.argv[1])
    print(reqs.headers.get("X-Request-Id"))