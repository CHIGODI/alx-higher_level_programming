#!/usr/bin/python3
import add_0 as add


def add_numbers():
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add.add(a, b)))


if __name__ == "__main__":
    add_numbers()
