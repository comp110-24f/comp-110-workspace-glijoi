"""list utility functions"""

__author__ = "730667690"


def only_evens(vals: list[int]) -> list[int]:
    """returns a list of even numbers from the input list"""
    idx: int = 0
    evens: list[int] = []
    while idx < len(vals):
        if vals[idx] % 2 == 0:
            evens.append(vals[idx])
            idx += 1
        else:
            idx += 1
    return evens


def sub(vals: list[int], start: int, end: int) -> list[int]:
    """returns a list that is a subset of the input list"""
    idx: int = 0
    subset: list[int] = []
    if start < 0:
        start = 0
    if end >= len(vals):
        end = len(vals)  # I initially added a -1 to the end but realized
        # this was causing errors
    while idx < len(vals):
        while idx < start:
            idx += 1
        if idx >= end:  # I had an error due to not including an =
            # I still had errors after, but that was
            # due to the issue in the previous comment
            return subset
        else:
            subset.append(vals[idx])
            idx += 1
    return subset


def add_at_index(vals: list[int], elem: int, index: int) -> None:
    """modifies input list to put elem at index"""
    if (index < 0) or (index > len(vals)):
        raise IndexError("Index is out of bounds for the input list")
    vals.append(0)
    for i in range(len(vals) - 1, index, -1):
        vals[i] = vals[i - 1]
    vals[index] = elem
