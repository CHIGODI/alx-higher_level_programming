#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        output = "{}{}, ".format(i, j)
        if output != 99:
            print(output, end='')

print("99")
