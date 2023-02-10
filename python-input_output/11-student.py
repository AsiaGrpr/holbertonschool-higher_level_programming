#!/usr/bin/python3
'''module to return Student to JSON with filter'''


class Student:
    '''
    Write a class Student that defines a student
    '''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        function that retrieves a dictionary representation
        of a Student instance, but If attrs is a list of strings,
        only attribute names contained in this list must be retrieved
        '''

        list = {}
        if attrs is not None:
            for key, value in self.__dict__.items():
                if key in attrs:
                    list[key] = value
            return (list)
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        '''
        Function that replace all attributes of the Student instance
        '''

        for key, value in json.items():
            self.__dict__[key] = value
