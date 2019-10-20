#!/usr/bin/python3
"""
first class Base
"""


class Base:
    """
    first class Base
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = Base.__nb_objects
