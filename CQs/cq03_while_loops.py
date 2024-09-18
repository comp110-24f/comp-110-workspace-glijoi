"""CQ03 - While Loops - practice with while loops"""

__author__ = "730667690"


def num_instances(phrase: str, search_char: str) -> None:
    """count number of instances a character appears in a phrase"""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    print(count)
