#!/usr/bin/python3
class Rectangle:
    """
    class Rectangle that defines a Rectangle 
    - width
    - height
    - area
    - perimeter
    - __str__
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height
        
    def __str__(self):
        rec = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            rec.append("#" * self.__width)
            rec.append("\n")
        return ("".join(rec))
        
    def __repr__(self):
        return ("Rectangle({}, {})".format(str(self.__width), str(self.__height)))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
