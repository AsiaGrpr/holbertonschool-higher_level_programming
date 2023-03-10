#!/usr/bin/python3
'''module to create a square'''


class Square:
    '''class to create a square, with size attribute to define its area'''

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        msg = "position must be a tuple of 2 positive integers"

        if type(value) is not tuple or len(value) != 2:
            raise TypeError(msg)
        for i in range(1):
            if type(value[i]) is not int or value[i] < 0:
                raise TypeError(msg)
        self.__position = value

    def area(self):
        return(self.__size**2)

    def my_print(self):
        if (self.__size == 0):
            print("")
        for space in range(self.__position[1]):
                print()
        for i in range(self.__size):
            for space in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
