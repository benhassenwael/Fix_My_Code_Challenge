#!/usr/bin/python3
""" Square Module"""


class square():
    """square class"""
    width = 0

    def __init__(self, *args, **kwargs):
        """init method """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiterOfMySquare(self):
        """ permiter of the square """
        return (self.width * 4)

    def __str__(self):
        """ printing the square """
        return "{0}/{0}".format(self.width)

if __name__ == "__main__":

    s = square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiterOfMySquare())
