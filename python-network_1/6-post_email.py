#!/usr/bin/python3
"""__summary__
- writes a script that takes in a URL and an email address
- sends a POST request to the URL with the email as a parameter
- and displays the body of the response (decoded in utf-8)
"""
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    reqs = requests.post(url, data=value)
    print(reqs.text)
