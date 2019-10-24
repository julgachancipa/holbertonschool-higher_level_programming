#!/usr/bin/python3
"""
first class Base
"""
import json
import os.path
import csv
import turtle
import random


class Base:
    """
    first class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init method
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        draw rectangles and squares with turtle
        """
        colors = ['Pale Green', 'Green Yellow', 'Forest Green',
                  'Turquoise', 'Slate Blue', 'Yellow',  'Cyan',
                  'Deep Pink', 'Orange Red']
        my_pen = turtle.Turtle()
        if list_rectangles is not None and len(list_rectangles) > 0:
            for rect in list_rectangles:
                my_pen.fillcolor(random.choice(colors))
                my_pen.up()
                my_pen.ht()
                my_pen.goto(rect.x, rect.y)
                my_pen.st()
                my_pen.down()
                my_pen.begin_fill()
                for side in range(2):
                    my_pen.forward(rect.width)
                    my_pen.right(90)
                    my_pen.forward(rect.height)
                    my_pen.right(90)
                my_pen.end_fill()

        if list_squares is not None and len(list_squares) > 0:
            for sqr in list_squares:
                my_pen.fillcolor(random.choice(colors))
                my_pen.up()
                my_pen.ht()
                my_pen.goto(sqr.x, sqr.y)
                my_pen.st()
                my_pen.down()
                my_pen.begin_fill()
                for side in range(4):
                    my_pen.forward(sqr.size)
                    my_pen.right(90)
                my_pen.end_fill()

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to json m
        """
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        to file method
        """
        if list_objs is not None and len(list_objs) > 0:
            lst = []
            for obj in list_objs:
                json_dict = obj.to_dictionary()
                lst.append(json_dict)
            with open(cls.__name__ + ".json", mode='w',
                      encoding='utf-8') as json_f:
                json_f.write(cls.to_json_string(lst))
        else:
            with open(cls.__name__ + ".json", mode='w',
                      encoding='utf-8') as json_f:
                json_f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        from json
        """
        l = []
        if json_string is not None:
            return json.loads(json_string)
        return l

    @classmethod
    def create(cls, **dictionary):
        """
        create method
        """
        if cls.__name__ is 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ is 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        from file
        """
        lst = []
        if os.path.isfile(cls.__name__ + '.json'):
            with open(cls.__name__ + ".json",
                      encoding='utf-8') as json_f:
                json_str = json_f.read()
                obj_dics = cls.from_json_string(json_str)
                for dicts in obj_dics:
                    lst.append(cls.create(**dicts))
                return lst
        else:
            return lst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save to file
        """
        if cls.__name__ is "Rectangle":
            headers = ["id", "width", "height", "x", "y"]
        elif cls.__name__ is "Square":
            headers = ["id", "size", "x", "y"]
        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as f:
            csv_writer = csv.DictWriter(f, fieldnames=(headers))
            csv_writer.writeheader()
            empty_list = []
            for i in list_objs:
                my_dict = i.to_dictionary()
                empty_list.append(my_dict)
                csv_writer.writerow(my_dict)
            return empty_list

    @classmethod
    def load_from_file_csv(cls):
        """
        from cvs files
        """
        lt = []
        if os.path.isfile(cls.__name__ + '.csv'):
            with open(cls.__name__ + '.csv',
                      encoding='utf-8') as csv_file:
                csv_write = csv.DictReader(csv_file)
                for dic in csv_write:
                    for key, value in dic.items():
                        dic[key] = int(value)
                    lt.append(cls.create(**dic))
                return lt
        else:
            return lt
