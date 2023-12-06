#!/usr/bin/python3


def uniq_add(my_list=[]):
    temp = set()
    sum = 0

    for num in my_list:
        temp.add(num)

    for num in temp:
        sum += num

    return sum
