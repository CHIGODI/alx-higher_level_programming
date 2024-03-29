#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the
URL and displays the value of the X-Request-Id variable found
in the header of the response.
"""

import urllib.request
import sys


def main():
    """
    Prints X-Request-Id variable found in the header of the response
    """
    with urllib.request.urlopen(sys.argv[1]) as req:
        response = req.headers.get('X-Request-Id')
        print(response)


if __name__ == '__main__':
    main()
