#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
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
    prev_ch = ""

    for ch in roman_string:
        if ch in my_dict:
            if prev_ch and my_dict[ch] > my_dict[prev_ch]:
                int_num += my_dict[ch] - my_dict[prev_ch] * 2
            else:
                int_num += my_dict[ch]
        prev_ch = ch
    return int_num
