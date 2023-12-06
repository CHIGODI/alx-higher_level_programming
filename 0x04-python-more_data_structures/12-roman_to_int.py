#!/usr/bin/python3


def roman_to_int(roman_string):
    if not roman_string or len(roman_string) == 0:
        return None

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

    for ch in roman_string:
        for key, value in my_dict.items():
            if ch == key:
                int_num += value
    return int_num
