#!/user/bin/python3


def multiply_by_2(a_dictionary):
    new = {}

    for key in a_dictionary:
        value = a_dictionary[key] * 2
        new.update({key: value})
    return new
