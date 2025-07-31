#!/usr/bin/python3
"""Displays X-Request-Id header value from a given URL"""
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    print(response.getheader("X-Request-Id"))
