"""Practice with conditionals."""


def less_than_10(num: int) -> None:
    """tell me if num is < 10"""
    if num < 10:
        print("Small number")
    else:
        print("Big number")
    print("Have a nice day")


less_than_10(num=11)


def should_i_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger"""
    if hungry:
        print("Eat some food")
    else:
        print("Do your comp homework")
    print("I'm proud of you <3")


should_i_eat(hungry=True)


def check_first_letter(word: str, letter: str) -> None:
    if letter == word[0]:
        print("match!")
    else:
        print("no match!")


check_first_letter(word="happy", letter="a")
