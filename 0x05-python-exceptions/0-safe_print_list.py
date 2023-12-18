#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element = 0
    try:
        while (element < x):
            print("{}".format(my_list[element]), end="")
            element = element + 1
        print()
    except Exception:
        print()
    return (element)
