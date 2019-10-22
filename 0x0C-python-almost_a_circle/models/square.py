#!/usr/bin/python3
"""
class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        init method
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        str method
        """
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y,
                       self.width))

    @property
    def size(self):
        """
        size g. method
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        size s. method
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        update method
        """
        if args is not None and len(args) > 0:
            for k in range(len(args)):
                if k == 0:
                    self.id = args[0]
                elif k == 1:
                    self.size = args[1]
                elif k == 2:
                    self.x = args[2]
                elif k == 3:
                    self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.width = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
        to dict method
        """
        o_d = self.__dict__
        names_list = ['x', 'y']
        d = {}
        for k in names_list:
            d[k] = o_d['_Rectangle__' + k]
        d['id'] = o_d['id']
        d['size'] = o_d['_Rectangle__width']
        return d
