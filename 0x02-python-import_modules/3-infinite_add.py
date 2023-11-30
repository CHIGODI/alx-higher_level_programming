#!/usr/bin/python3
import sys


def infinite_add():
    infinite_sum = 0
    arguments = sys.argv
    for x in range(1, len(arguments)):
        infinite_sum += int(arguments[x])

    print("{:d}".format(infinite_sum))


if __name__ == "__main__":
    infinite_add()
