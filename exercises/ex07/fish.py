"""File to define Fish class."""

__author__ = "730667690"


class Fish:
    """Creates an instance of a fish in the river."""

    age: int

    def __init__(self):
        """Initializes."""
        self.age = 0
        return None

    def one_day(self):
        """Ages fish by one day."""
        self.age += 1
        return None
