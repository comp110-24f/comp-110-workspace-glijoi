"""dictionary"""

__author__ = "730667690"


def invert(input: dict[str, str]) -> dict[str, str]:
    """invert keys and values of dictionary input"""
    inverted = {}
    keys: list[str] = list(input.keys())
    values: list[str] = list(input.values())
    index: int = 0
    check = list()
    for i in values:
        if i in check:
            raise KeyError("You cannot have duplicates of a key!")
        else:
            check.append(i)

    while len(values) == len(keys) and index < len(values):
        inverted[values[index]] = keys[index]
        index += 1
    return inverted


def favorite_color(input: dict[str, str]) -> str:
    """takes people's favorite colors and returns the most frequent color"""
    counts: dict[str, int] = {}
    for key in input:
        if input[key] in counts:
            counts[input[key]] += 1
        else:
            counts[input[key]] = 1
    count_values: list[int] = list(counts.values())
    count_colors: list[str] = list(counts.keys())
    majority: int = 0
    index: int = 0
    color: str = ""
    while index < len(count_values):
        if count_values[index] == majority:
            count_values.pop(index)
        elif count_values[index] > majority:
            majority = count_values[index]
        index += 1
    index = count_values.index(majority)
    color += count_colors[index]
    return color


def count(input: list[str]) -> dict[str, int]:
    """counts number of times a each value appears in the list"""
    counted: dict[str, int] = {}
    for i in input:
        if i in counted:
            counted[i] += 1
        else:
            counted[i] = 1
    return counted


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """sorts words by first letter"""
    letters: dict[str, list[str]] = {}
    for word in input:
        letter: str = word[0].lower()
        if letter in letters:
            letters[letter].append(word)
        else:
            letters[letter] = [word]
    return letters


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    """updates the attendance"""
    if day in input:
        if student not in input[day]:
            input[day].append(student)
        else:
            input[day] = [student]
