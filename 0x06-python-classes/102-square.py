#!/usr/bin/python3
class Square:
    """
    Write a class Square that defines a square by:
    (based on 3-square.py)
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def __eq__(self, other):
        return ((self.size) == (other.size))

    def __ne__(self, other):
        return ((self.size) != (other.size))

    def __lt__(self, other):
        return ((self.size) < (other.size))

    def __le__(self, other):
        return ((self.size) <= (other.size))

    def __gt__(self, other):
        return ((self.size) > (other.size))

    def __ge__(self, other):
        return ((self.size) >= (other.size))

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
