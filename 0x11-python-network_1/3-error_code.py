#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
or display error code
"""

import sys
import urllib.request


def main():
    """
    request to the URL and displays the body of the response
    (decoded in utf-8). or display error code
    """
    try:
        with urllib.request.urlopen(sys.argv[1]) as req:
            response = req.read()
            content_utf = response.decode('utf-8')
            print(content_utf)
    except urllib.error.URLError as e:
        print(f'Error code: {e.code}')


if __name__ == '__main__':
    main()
