"""Summing the elements of a list using different loops"""

__author__ = "730667690"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for elem in range(0, len(vals)):
        sum += elem
    return sum


# DELETE AND RUN THIS COMMAND TO SUBMIT: python -m tools.submission CQs/cq06_sum.py
