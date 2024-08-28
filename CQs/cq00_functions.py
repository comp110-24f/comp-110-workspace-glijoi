"""functions challenge question"""

__author__ = "730667690"


def mimic(message: str) -> str:
    """returns message back"""
    return message


def main() -> None:
    """print result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
