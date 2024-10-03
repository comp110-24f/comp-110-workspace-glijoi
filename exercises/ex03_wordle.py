"""Wordle game"""

__author__ = "730667690"


def input_guess(secret_word_len: int) -> str:
    """check that guess is correct length"""
    word = str(input(f"Enter a {secret_word_len} character word:"))
    while len(word) != secret_word_len:
        word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return word


def contains_char(word: str, letter: str) -> bool:
    """checks each character of guess for the letter"""
    assert len(letter) == 1
    idx: int = 0
    while idx <= len(word):
        if idx == len(word):
            return False
        elif word[idx] == letter:
            return True
        else:
            idx += 1


def emojified(guess: str, secret: str) -> str:
    """returns a string of emojis signaling which letters and placement are correct"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    index: int = 0
    while index < len(guess):
        if guess[index] == secret[index]:
            result += GREEN_BOX
        elif contains_char(word=secret, letter=guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 0
    max: int = 6
    win: bool = False
    while turns < max and not win:
        turn += 1
        print(f"=== {turn}/6 ===")
        guess = input_guess(secret_word_len=len(secret))
        result = emojified(guess, secret)
        print(result)
        if guess == secret:
            win = True
    if win:
        print(f"You won in {turn}/{max} turns!")
    else:
        print(f"X/{max} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
