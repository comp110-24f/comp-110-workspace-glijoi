"""EX02 - Chardle - a cute step towards Wordle."""

__author__ = "730667690"


def input_word() -> str:
    """asks the user for a word"""
    word = str(input("Enter a 5-character word: "))
    if len(word) == 5:
        print(word)
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()


def input_letter() -> str:
    """asks the user for a letter"""
    letter = str(input("Enter a single character: "))
    if len(letter) == 1:
        print(letter)
        return letter  # I initially forgot that the result should be a return value as well as printed
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    """Check for letter in word"""
    count: int = 0
    index: int = 0
    print("Searching for " + letter + " in " + word)
    while index < len(
        word
    ):  # I outlined each index as an individual if else function, but then later changed it into a while loop with local variables
        if word[index] == letter:
            print(letter + " found at index " + str(index))
            count += 1
        index += 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    """Call the functions"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
