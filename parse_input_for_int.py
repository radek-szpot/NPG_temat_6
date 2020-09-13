#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The module checks whether input is numerical and is in given range.
"""


def parse_input_for_int(min, max):
    user_input = input()
    try:
        num = int(user_input)
    except ValueError:
        print("Proszę podać liczbę")
        return parse_input_for_int(min, max)

    if min is not None and max is not None:
        if num > max or num < min:
            print("Podana liczba nie jest z przedziału {} do {}".format(min, max))
            return parse_input_for_int(min, max)
    else:
        if min is not None and num < min:
            print("Podana liczba jest mniejsza od {}".format(min))
            return parse_input_for_int(min, max)
        if max is not None and num > max:
            print("Podana liczba jest większa od {}".format(max))
            return parse_input_for_int(min, max)

    return num
