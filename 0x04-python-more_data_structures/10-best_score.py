#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    dict_copy = list(a_dictionary.items())
    best_score = dict_copy[0][1]
    keys = ""
    for key, value in a_dictionary.items():
        if value > best_score:
            best_score = value
            keys = key
    return keys
