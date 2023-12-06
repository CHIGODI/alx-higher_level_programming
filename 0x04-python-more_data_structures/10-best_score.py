#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    keys = ""
    dict_copy = list(a_dictionary.values())
    best_score = dict_copy[0]
    key for key, value in a_dictionary.items():
        if value > best_score:
            best_score = value
            keys = key
    return keys
