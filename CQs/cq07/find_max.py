""""""

__author__ = "730667690"


def find_and_remove_max(vals: list[int]) -> int:
    """find and return largest # in list AND remove all instances of largest #"""
    if len(vals) == 0:
        return -1
    else:
        big: int = 0
        idx: int = 0
        while idx < len(vals):
            if vals[idx] > big:
                big = vals[idx]
            idx += 1
        idx = 0
        while idx < len(vals):
            if vals[idx] == big:
                vals.pop(idx)
            else:
                idx += 1
        return big
