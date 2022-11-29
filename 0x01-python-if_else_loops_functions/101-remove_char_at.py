#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    for char in str:
        if (char != n):
            copy = copy + str[char]
    return copy
