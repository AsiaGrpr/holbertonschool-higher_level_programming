#!/usr/bin/python3
'''module First Rectangle with class inherited'''


from models.base import Base


class Rectangle(Base):
    '''class to create a rectangle with width and height attribute'''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''function that define area of the rectangle'''

        return self.__height * self.__width

    def display(self):
        '''method that prints in stdout the Rectangle instance
        with the character #'''

        for y in range(0, self.__y):
            print("")
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        '''method so that it returns [Rectangle] (<id>) <x>/<y> -
        <width>/<height>'''

        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        '''method that assigns an argument to each attribute'''

        if args:
            if len(args) > 0:
                try:
                    self.id = args[0]
                    self.__width = args[1]
                    self.__height = args[2]
                    self.__x = args[3]
                    self.__y = args[4]
                except IndexError:
                    pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''method that returns the dictionary representation of a Rectangle'''

        return dict(id=self.id, width=self.__width, height=self.__height,
                    x=self.__x, y=self.__y)
