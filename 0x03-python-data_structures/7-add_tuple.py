#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    num1 = 0
    num2 = 0

    for num in tuple_a:
        if num is tuple_a[0]:
            num1 = num + num1
        elif num is tuple_a[1]:
            num2 = num2 + num
    for num in tuple_b:
        if num is tuple_b[0]:
            num1 += num
        elif num is tuple_b[1]:
            num2 += num
    return (num1, num2)
