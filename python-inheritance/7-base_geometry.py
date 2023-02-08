#!/usr/bin/python3
'''module to create empty class'''


class BaseGeometry():
    '''empty class to create'''

    def __init__(self):
        '''init method'''

        pass

    def area(self):
        '''area method'''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''method to validate the value'''

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    pass
