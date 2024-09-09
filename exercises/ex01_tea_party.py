"""Exercise to plan logistics for a tea party."""

__author__ = "730667690"


def main_planner(guests: int) -> None:
    """Entrypoint of tea party planning program."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# the only part that was particularly challenging for me was the final print line.
# I initially put the mathematics in and then reviewed the directions
# saying that was not an option. Then I messed around with different inputs
# until I realized that a function call could exist within another function call.


def tea_bags(people: int) -> int:
    """Calculate number of tea bags needed."""
    return people * 2


def treats(people: int) -> int:
    """Calculate number of treats needed based on number of teas."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the total cost of tea and treats."""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
