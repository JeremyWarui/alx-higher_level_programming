#!/usr/bin/python3
def max_integer(my_list=[]):
    nums = len(my_list)
    max = my_list[0]
    if nums == 0:
        return None
    else:
        for n in my_list:
            if n > max:
                max = n
    return max
