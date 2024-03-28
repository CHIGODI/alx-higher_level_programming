#!/usr/bin/python3
"""
A Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""

import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        response = res.read()
        r = response.decode('utf-8')
        print(r)
