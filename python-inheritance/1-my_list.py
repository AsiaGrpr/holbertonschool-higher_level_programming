#!/usr/bin/python3
'''module where I had to Write a class MyList that inherits'''


class MyList(list):
    '''class which inherits and had one method to print the list inherited'''

    def print_sorted(self):
        '''method that prints the list, but sorted (ascending sort)'''

        print(sorted(self))
