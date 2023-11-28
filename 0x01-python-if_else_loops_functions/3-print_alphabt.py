#!/usr/bin/python3
output = ''
i = 97
for i in range(97, 123):
    if i != 101 and i != 113:
        output += '{}'.format(chr(i))
print(output, end='')
