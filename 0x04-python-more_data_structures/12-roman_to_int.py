#!/usr/bin/python3


def roman_to_int(roman_string):
    my_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    int_num = 0

    if not roman_string or roman_string == 0:
        return None

    for ch in roman_string:
        for key, value in my_dict.items():
            if ch == key:
                ch = value
                int_num += ch
    return int_num
