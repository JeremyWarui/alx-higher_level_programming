#!/usr/bin/python3
def best_score(a_dictionary):
    """
    function to find max value in a dictionary
    """
    if not a_dictionary:
        return None
    else:
        return max(a_dictionary, key=lambda x: a_dictionary[x])
