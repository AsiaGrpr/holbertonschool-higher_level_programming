#!/usr/bin/python3
'''module to create inherited class'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Class that inherits with class parent: Rectangle'''

    def __init__(self, size):
        '''init method'''

        super().integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        '''area methode for this child class'''

        return (self.__size * self.__size)
