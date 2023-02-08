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

    pass
