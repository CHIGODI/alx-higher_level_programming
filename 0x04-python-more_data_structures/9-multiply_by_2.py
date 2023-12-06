#!/user/bin/python3


def multiply_by_2(a_dictionary):
    new = {}

    for key in a_dictionary:
        new.update({key: a_dictionary.get(key) * 2})
    return new
