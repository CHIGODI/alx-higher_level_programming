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
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    response = requests.get(url)
    res = response.json()

    try:
        for i in range(10):
            print(
                f"{res[i].get('sha')}: "
                f"{res[i].get('commit').get('author').get('name')}"
                )
    except Exception as e:
        pass
