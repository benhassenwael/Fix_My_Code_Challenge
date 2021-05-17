#!/usr/bin/python3
""" Square Module"""


class Square():
    """square class"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ constructor """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiter_of_my_square(self):
        """ permiter of the square """
        return (self.width * 4)

    def __str__(self):
        """ printing the square """
        return "{0}/{0}".format(self.width)

if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
