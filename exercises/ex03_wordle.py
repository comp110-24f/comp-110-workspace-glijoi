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
    return letter in word
    # instead of using "return letter in word" I tried to
    # create a lengthy function that manually checked each
    # letter and returned True or False, which doesn't work
    # unless the return type is None, so I fixed that


def emojified(guess: str, secret: str) -> str:
    """returns a string of emojis signaling which letters and placement are correct"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    # I got stuck when trying to print the result until
    # I realized I needed to start with a blank string
    # as a variable
    index: int = 0
    while index < len(guess):
        if guess[index] == secret[index]:
            result += GREEN_BOX
        elif contains_char(word=secret, letter=guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 0
    max: int = 6
    win: bool = False
    while turn < max and not win:
        turn += 1
        print(f"=== Turn {turn}/{max} ===")
        # I initially forgot the word Turn so I fixed that
        guess = input_guess(secret_word_len=len(secret))
        emoji_result = emojified(guess, secret)
        print(emoji_result)
        if guess == secret:
            win = True
    if win is True:
        print(f"You won in {turn}/{max} turns!")
    else:
        print(f"X/{max} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
