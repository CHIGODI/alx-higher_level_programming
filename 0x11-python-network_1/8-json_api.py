#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display
the id and name like this: [<id>] <name>
    Otherwise:
    Display Not a valid JSON if the JSON is invalid
    Display No result if the JSON is empty
"""

import sys
import requests


if __name__ == '__main__':
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post(
        'http://0.0.0.0:5000/search_user',
        data={'q': letter}
        )

    if response.headers.get('content-type') == 'application/json':
        if response.json():
            id = response.json().get('id')
            name = response.json().get('name')
            print(f'[{id}] {name}')
        else:
            print('No result')
    else:
        print('Not a valid JSON')
