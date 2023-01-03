#!/usr/bin/python3
"""Module containing the Square class"""


class Square:
    """The Square class"""
    def __init__(self, size=0):
        """Initializing an instance of Square

        Args:
            size (int): The size of the Square instance. default value is 0.

         """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValuError("size must be >= 0")

        self.__size = size
