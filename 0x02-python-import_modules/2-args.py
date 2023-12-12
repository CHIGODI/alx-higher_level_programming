#!/usr/bin/python3
import sys


def print_arguments():
    x = 1
    count = -1
    argmts = sys.argv

    for i in range(0, len(argmts)):
        count += 1

    if count == 0:
        print("0 arguments.")
    elif len(argmts) == 2:
        print("1 argument:")
        print("1: {}".format(argmts[1]))
    elif len(argmts) > 2:
        print("{} arguments:".format(count))
        while x != len(argmts):
            print("{}: {}".format(x, argmts[x]))
            x += 1


if __name__ == "__main__":
    print_arguments()
