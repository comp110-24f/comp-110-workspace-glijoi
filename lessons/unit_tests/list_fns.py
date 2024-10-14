"""unit tests practice"""


def get_first(vals: list[str]) -> str:
    """takes a list and returns first element"""
    return vals[0]


def remove_first(vals: list[str]) -> None:
    """takes a list and removes first element"""
    vals.pop(0)


def get_and_remove_first(vals: list[str]) -> str:
    """takes list and returns + removes first element"""
    first: str = get_first(vals)
    remove_first(vals)
    return first
