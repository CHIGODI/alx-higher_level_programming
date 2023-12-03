#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    rem = my_list[idx]
    new = my_list[:]
    my_list.clear()
    for item in new:
        if item is not rem:
            my_list.append(item)

    return my_list
