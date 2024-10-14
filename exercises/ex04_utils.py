"""list utility functions"""

__author__ = "730667690"


def all(vals: list[int], number: int) -> bool:
    """check if all list values equal the number"""
    sum: float = 0
    i: int = 0
    if len(vals) == 0:
        return False
    else:
        while i < len(vals):
            sum += vals[i]
            i += 1
        sum /= i  # this takes the sum of all values in the list
        # and divides them by the number of values, which mathematically
        # speaking should result in the same number as the number input if
        # each value in the list is equal to that number
        return sum == number


def max(input: list[int]) -> int:
    """returns the largest number in the list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        idx: int = 1
        max: int = input[0]
        while idx < len(input):
            if input[idx] > max:
                max = input[idx]  # this line replaces the current max with any
                # larger number that appears later in the list
            idx += 1
        return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """check if each value at every index of one list is the same as the other list"""
    idx: int = 0
    number1: int = 0
    number2: int = 0
    # these number variables allow each individual value at the same index to be
    # compared to each other without comparing entire lists
    if len(list1) != len(list2):
        return False
    elif len(list1) == 0 and len(list2) == 0:
        return True
    elif len(list1) == 0 or len(list2) == 0:
        return False
    else:
        while idx < len(list1):
            number1 = list1[idx]
            number2 = list2[idx]
            if number1 != number2:
                return False
            else:
                idx += 1
        return list1 == list2


def extend(list1: list[int], list2: list[int]) -> None:
    """adds values of the second list to the end of the first list"""
    idx: int = 0
    val: int = 0
    while idx < len(list2):
        val = list2[idx]  # by using this val variable, each value in
        # list2 is considered separately from the list and can therefore
        # be added to list1 one at a time
        list1.append(val)
        idx += 1
