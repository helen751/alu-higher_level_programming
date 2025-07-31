#!/usr/bin/python3
"""__summary__
- writes a script that takes in a URL as a command line argument
- sends a request to the URL
- and displays the body of the response
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as resq:
            print(resq.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
