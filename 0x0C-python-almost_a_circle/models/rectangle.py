#!/usr/bin/python3
"""
class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return self.__width * self.__height

    def display(self):
        print("\n" * self.__y, end='')
        for i in range(self.__height):
            print((self.__x * " ") + (self.__width * "#"))

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.__x, self.__y,
                       self.__width, self.__height))

    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            for k in range(len(args)):
                if k == 0:
                    Base.__init__(self, args[0])
                elif k == 1:
                    self.width = args[1]
                elif k == 2:
                    self.height = args[2]
                elif k == 3:
                    self.x = args[3]
                elif k == 4:
                    self.y = args[4]
        else:
            if 'id' in kwargs:
                Base.__init__(self, kwargs['id'])
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
