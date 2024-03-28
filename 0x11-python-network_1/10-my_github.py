#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.post('https://api.github.com/user', auth=basic)
    print(response.json().get('id'))
