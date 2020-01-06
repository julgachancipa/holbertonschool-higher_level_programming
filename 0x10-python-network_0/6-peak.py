#!/usr/bin/python3
""" function find_peak """


def find_peak(list_of_integers):
    """find pick"""
    if list_of_integers:
        p = list_of_integers[0]
        for i in range(1, len(list_of_integers) - 1):
            if list_of_integers[i] > list_of_integers[i - 1]\
               and list_of_integers[i] > list_of_integers[i + 1]:
                p = list_of_integers[i]
        return p
    else:
        return None
