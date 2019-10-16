#!/usr/bin/python3
"""
class MyInt that inherits from int
"""


class MyInt(int):
    """
    class MyInt that inherits from int
    """
    def __init__(self, val):
        self.__val = val

    def __ne__(self, other):
        return not self.__val.__eq__(other)

    def __eq__(self, other):
        return not self.__val.__ne__(other)
