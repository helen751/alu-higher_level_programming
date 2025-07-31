#!/usr/bin/python3
"""__summary__
- writes a script that takes in a URL
- sends a request to the URL
- handling HTTP errors by displaying the error code
"""
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]

    reqs = requests.get(url)
    if reqs.status_code >= 400:
        print('Error code: {}'.format(reqs.status_code))
    else:
        print(reqs.text)
