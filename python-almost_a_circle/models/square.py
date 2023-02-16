#!/usr/bin/python3
'''module And now, the Square! with class inherited: parent = Rectangle'''


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class Square that inherits from Rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.width = value
            self.height = value
        else:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')

    def __str__(self):
        '''method should return [Square] (<id>) <x>/<y> - <size>'''
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y,
                       self.width))

    def update(self, *args, **kwargs):
        '''method that assigns an argument to each attribute'''

        if args:
            if len(args) > 0:
                try:
                    self.id = args[0]
                    self.size = args[1]
                    self.x = args[2]
                    self.y = args[3]
                except IndexError:
                    pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
