#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    function that gives average weight score
    """
    if my_list is not None:
        numerator = 0
        denominator = 0
        for tup in my_list:
            numerator += tup[0] * tup[1]
            denominator += tup[1]
        return numerator / denominator
    else:
        return 0
