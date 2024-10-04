"""Mutating functions."""

__author__ = "730667690"


def manual_append(list: list[int], number: int) -> None:
    """add number to the end of the list"""
    list.append(number)


def double(list: list[int]) -> None:
    """mutate by multiplying each value in list by 2"""
    index: int = 0
    while index < len(list):
        list[index] *= 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
