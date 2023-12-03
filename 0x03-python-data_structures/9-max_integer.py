#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list == None:
        return None

    large = my_list[0]
    for element in my_list:
        if element > large:
            large = element
            return large
