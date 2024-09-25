"""Practice with conditionals, local variables, and user input."""

__author__ = "730667690"


def guess_a_number() -> None:
    """Have the user guess a number"""
    secret = 7
    guess = int(input("Guess a number: "))
    print("Your guess was " + str(guess))
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is 7.")
    else:  # no need to go into the > specification since that is the only exception to
        # other rules
        print("Your guess was too high! The secret number is 7.")


if __name__ == "__main__":
    guess_a_number()
