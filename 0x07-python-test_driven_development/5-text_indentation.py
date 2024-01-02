#!/usr/bin/python3

"""
   manipulating text module
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for ch in text:
        if ch in [':', '?', '.']:
            print('\n')
        else:
            print(ch, end='')
