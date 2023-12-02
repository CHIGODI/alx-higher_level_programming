#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    copy_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return my_list
    copy_list[idx] = element
    return copy_list
