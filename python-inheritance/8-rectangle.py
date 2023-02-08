#!/usr/bin/python3
'''module to create inherited class'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class that inherits with class parent: BaseGeometry'''

    def __init__(self, width, height):
        '''init method'''

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    pass
