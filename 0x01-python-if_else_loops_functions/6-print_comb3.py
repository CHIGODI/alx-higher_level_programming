#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        output = "{}{}, ".format(i, j)
        if (i, j) != (8, 9) and i != j:
            print(output, end='')
print('89')
