#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    function that sorts the dict using keys
    """
    list_d = list(a_dictionary.keys())
    list_d.sort()
    for key in list_d:
        print("{}: {}".format(key, a_dictionary.get(key)))
