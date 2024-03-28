#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status and prints
a formated body of the response
"""

import requests


if __name__ == '__main__':
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print(
        f'Body response:\n'
        f'\t- type: {type(response.text)}\n'
        f'\t- Content: {response.text}'
          )
