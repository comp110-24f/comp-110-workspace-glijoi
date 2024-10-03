# comparing lists and strings:
a: str = "24"
b: str = a
a += "6"
print(b)
# output is 24

a: list[int] = [2, 4]
b: list[int] = a
a.append(6)
print(b)
# output is [2,4,6]


# Taking list as argument
def display(vals: list[int]) -> None:
    idx: int = 0
    while idx < len(vals):
        print(vals[idx])
        idx += 1


display([1, 2, 3])
# output:
# 1
# 2
# 3


# Creating and Returning a List
def odds_list(min: int, max: int) -> list[int]:
    """returns list of odds between min and max"""
    odds: list[int] = list()
    x: int = min
    while x <= max:
        if x % 2 == 1:
            odds.append(x)
        x += 1
    return odds


global_odds: list[int] = odds_list(2, 6)
print(global_odds)
# output is [3,5]


# Modifying a List
def remove_first(xs: list[str]):
    xs.pop(0)


course: list[str] = ["Comp", "110"]
remove_first(course)
# in order to see an output, must add the following:
print(course)
# output is ['110']
