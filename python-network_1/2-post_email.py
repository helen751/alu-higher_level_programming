#!/usr/bin/python3
"""Sends a POST request to a URL with an email as parameter"""
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]
data = urllib.parse.urlencode({'email': email}).encode('ascii')

req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    print(response.read().decode('utf-8'))
