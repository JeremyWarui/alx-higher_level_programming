#!/usr/bin/python3
def no_c(my_string):
    copy = my_string[:]
    list_copy = list(copy)
    for char in list_copy:
        if char == "c" or char == "C":
            list_copy.remove(char)
    new_list = "".join(list_copy)
    return new_list
