#!/usr/bin/python3
for alpha in range(26, 0, -1):
    if (alpha % 2 == 0):
        print("{:c}".format(96 + alpha), end="")
    else:
        print("{:c}".format(64 + alpha), end="")
