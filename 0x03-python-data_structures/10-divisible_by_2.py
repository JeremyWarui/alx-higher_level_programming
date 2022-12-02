#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    copy = []
    for n in my_list:
        if n % 2 is 0:
            copy.append(True)
        else:
            copy.append(False)
    return copy
