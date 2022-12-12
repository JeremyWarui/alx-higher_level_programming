#!/usr/bin/python3
def roman_to_int(roman_string):
    digit = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string and type(roman_string) is str:
        total = 0
        for roman in reversed(roman_string):
            arabic = digit[roman]
            total += arabic if total < (arabic * 5) else -arabic
        return total
