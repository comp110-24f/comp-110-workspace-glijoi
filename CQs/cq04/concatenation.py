"""concatenation"""

__author__ = "730667690"


def concat(str1: str, str2: str) -> str:
    """concatenates the two strings"""
    return str1 + str2


if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(str1=word1, str2=word2))
