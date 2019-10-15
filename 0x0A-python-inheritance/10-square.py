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
    the area() method must be implemented
    print() should print, and str() should return,
    the following rectangle description: [Rectangle] <width>/<height>
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    Square that inherits from Rectangle
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size
