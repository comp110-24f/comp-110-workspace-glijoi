"""Basic syntax of lists"""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

print(my_numbers)

# add values:
my_numbers.append(1.5)
my_numbers.append(2.3)
print(my_numbers)  # not technically needed since print statement above

# create already populated list:
game_points: list[int] = [102, 86, 94]
print(game_points)

# Subscription notation and indexing:
print(game_points[2])
last_game: int = game_points[2]
print(last_game)

# modify by index, lists are mutable but not strings
game_points[1] = 72
print(game_points)

# get length
len(game_points)

# remove item
game_points.pop(1)
print(game_points)


def display(int_list: list[int]) -> None:
    """displays all elements of int_list"""
    index: int = 0
    while index < len(int_list):
        print(int_list[index])
        index += 1


display(int_list=game_points)
