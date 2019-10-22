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
        """
        init method
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        area method
        """
        return self.__width * self.__height

    def display(self):
        """
        display method
        """
        print("\n" * self.__y, end='')
        for i in range(self.__height):
            print((self.__x * " ") + (self.__width * "#"))

    def __str__(self):
        """
        str method
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.__x, self.__y,
                       self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        update method
        """
        if args is not None and len(args) > 0:
            for k in range(len(args)):
                if k == 0:
                    self.id = args[0]
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
                self.id = kwargs['id']
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
        """
        width getter method
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter method
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        height getter method
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter method
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        x getter method
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x getter method
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y getter method
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter method
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def to_dictionary(self):
        """
        to dict method
        """
        o_d = self.__dict__
        names_list = ['width', 'height', 'x', 'y']
        d = {}
        for k in names_list:
            d[k] = o_d['_Rectangle__' + k]
        d['id'] = o_d['id']
        return d
