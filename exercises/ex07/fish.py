"""File to define Fish class."""

__author__ = "730667690"


class Fish:
    """creates an instance of a fish in the river"""

    age: int

    def __init__(self):
        """initializes"""
        self.age = 0
        return None

    def one_day(self):
        """ages fish by one day"""
        self.age += 1
        return None
