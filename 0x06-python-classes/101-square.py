#!/usr/bin/python3
class Square:
    """
    Write a class Square that defines a square by:
    (based on 5-square.py)
    """
    def __init__(self, size=0,  position=(0, 0)):
        self.size = size
        self.position = position

    def __str__(self):
        s_list = []
        if self.__size:
            s_list.append("\n" * self.__position[1])
            for i in range(self.__size):
                s_list.append(" " * self.__position[0])
                for j in range(self.__size):
                    s_list.append("#")
                if (self.__size - 1) != i:
                    s_list.append("\n")
        else:
            s_list.append("\n")
        return ("".join(s_list))

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2\
           or type(value[0]) != int or type(value[1]) != int\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.__size:
            print("\n" * self.__position[1], end='')
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                for j in range(self.__size):
                    print("#", end='')
                print('')
        else:
            print('')
