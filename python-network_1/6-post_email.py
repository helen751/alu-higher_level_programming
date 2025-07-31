#!/usr/bin/python3
"""POST an email to a URL using requests and print the response"""
import requests
import sys

url = sys.argv[1]
email = sys.argv[2]
data = {'email': email}
r = requests.post(url, data=data)
print(r.text)
