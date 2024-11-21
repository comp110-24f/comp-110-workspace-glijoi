"""Working with Linked Lists."""

from __future__ import annotations

__author__ = "730667690"


class Node:
    """Item for a linked list."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Construct linked list."""
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


def value_at(head: Node | None, index: int) -> int:
    """Returns the data of a node at the index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.value
    else:
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
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
    if len(items) == 0:
        return None
    if len(items) == 1:
        return Node(items[0], None)
    else:
        return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns linked list of nodes where each node is multiplied by the factor."""
    if head is None:
        return None
    else:
        return Node(head.value * factor, scale(head.next, factor))
