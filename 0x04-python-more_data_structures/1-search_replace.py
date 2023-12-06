#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new = []

    for num in my_list:
        if num == search:
            num = replace
            new.append(num)
        else:
            new.append(num)

    return new
