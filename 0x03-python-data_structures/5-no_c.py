#!/usr/bin/python3


def no_c(my_string):
    cp_my_string = ""
    for ch in my_string:
        if ch != 'C' and ch != 'c':
            cp_my_string += ch
    return cp_my_string
