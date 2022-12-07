#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    function that replaces the value or
    adds the key value pair if key not present
    """
    a_dictionary[key] = value
    return a_dictionary
