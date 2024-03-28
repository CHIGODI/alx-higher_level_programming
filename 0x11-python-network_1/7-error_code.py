#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the
body of the response.
If the HTTP status code is greater than or equal to 400,
    - prints: Error code: followed by the value of the HTTP status code
"""

import sys
import requests


if __name__ == '__main__':
    response = requests.get(sys.argv[1])

    if response.status_code >= 400:
        print(f'Error code: {response.status_code}')
    else:
        print(response.text)
