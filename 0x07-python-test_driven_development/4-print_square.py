#!/usr/bin/python3

"""Create function print_square"""


def print_square(size):
    """This function that prints a square with the character #"""
    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) in [float] and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
