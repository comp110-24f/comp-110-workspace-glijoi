from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        if self.next is None:
            rest = "None"
        else:
            rest = self.next.__str__()
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))


def to_str(head: Node | None) -> str:
    """Represent a linked list as a string."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    print(f"Enter last ({head.value})")
    if head.next is None:
        print(f"Return base case: {head.value}")
        return head.value
    else:
        rest: int = last(head.next)
        print(f"Return recur: {head.value} -> {rest}")
        return rest


def value_at(head: Node | None, index: int) -> int:
    """Returns the data of a node at the index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.value
    else:
        return value_at(head.next, index - 1)


def max(head: Node | None):
    """Returns the max data value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    else:
        max_rest = max(head.next)
        if head.value > max_rest:
            return head.value
        else:
            return max_rest


def linkify(items: list[int]) -> Node | None:
    """Returns a linked list of nodes with the values from the input list."""
    if not items:
        return None
    else:
        return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns linked list of nodes where each node is multiplied by the factor."""
    if head is None:
        return None
    else:
        scaled_next = scale(head.next, factor)
        return Node(head.value * factor, scaled_next)
