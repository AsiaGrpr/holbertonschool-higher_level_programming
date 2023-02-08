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

    def area(self):
        '''area methode for this child class'''

        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    pass
