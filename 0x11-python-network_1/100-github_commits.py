#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
Uses the GitHub API, here is the documentation:
    - https://developer.github.com/v3/repos/commits/
"""

import requests
import sys


if __name__ == '__main__':
    url = f'https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits'
    header = {"Accept": "application/vnd.github+json"}
    response = requests.get(url, headers=header)
    res = response.json()

    for i in range(0, 10):
        print(
            f"{res[i].get('sha')}: "
            f"{res[i].get('commit').get('author').get('name')}"
            )
