#!/usr/bin/python3
def remove_char_at(str, n):
    output = ""
    count = -1
    for letter in str:
        count = count + 1
        if count == n:
            count += 1
            continue
        output += letter
    return output
