#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    dict_copy = list(a_dictionary.items())
    best_score = dict_copy[0][1]

    for key, value in a_dictionary.items():
        if value > best_score:
            best_score = value
    return best_score
