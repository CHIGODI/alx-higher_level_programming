#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request


def main():
    """
    feteches url and displays body
    """
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as req:
        response = req.read()
        utf_content = response.decode('utf-8')
        print(f'Body response:\n\t'
              f'- type: {type(response)}\n\t'
              f'- content: {response}\n\t'
              f'- utf content: {utf_content}'
              )


if __name__ == '__main__':
    main()
