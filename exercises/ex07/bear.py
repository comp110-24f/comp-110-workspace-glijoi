"""File to define Bear class."""

__author__ = "730667690"


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        """initializes"""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """ages bear by one day"""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """bear hunger change based on fish eaten"""
        self.hunger_score += num_fish
        return None
