#!/usr/bin/python3
class BaseGeometry:
    """
    -Public instance method: def area(self): that raises
    an Exception with the message area() is not implemented
    -Public instance method: def integer_validator(self, name, value):
    that validates value
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Instantiation with width and height: def __init__(self, width, height)
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
