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

    if not roman_string or roman_string == None or len(roman_string) == 0:
        return None

    for ch in roman_string:
        if ch in my_dict:
            int_num += my_dict[ch]
    return int_num
