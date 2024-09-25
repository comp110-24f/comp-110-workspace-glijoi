"""practice with scope"""


def remove_chars(msg: str, char: str) -> str:
    """returns a copy of msg that removes all instances of char from msg"""
    copy: str = ""  # sets up an empty string to copy values over
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]
        index += 1
    return copy


if __name__ == "__main__":
    word: str = "yoyo"
    print(remove_chars(msg=word, char="y"))
