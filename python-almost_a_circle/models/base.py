#!/usr/bin/python3
'''models module'''


import json


class Base():
    '''class base'''

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''method that returns the JSON string
        representation of list_dictionaries'''

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''class method that writes the JSON string
        representation of list_objs to a file'''

        new = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for i in list_objs:
                new.append(i.to_dictionary())
        json_string = cls.to_json_string(new)
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        '''method that returns the list of the JSON string
        representation json_string'''

        if json_string is not None or json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        '''method that returns an instance with all attributes already set'''

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                return [cls.create(**dict) for
                        dict in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []
