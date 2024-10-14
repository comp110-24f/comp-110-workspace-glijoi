"""Test functions of find_max"""

__author__ = "730667690"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_return() -> None:
    """find_and_remove_max should return biggest number in list"""
    vals = [10, 9, 8, 7, 10]
    assert find_and_remove_max(vals) == 10


def test_find_and_remove_max_mutate() -> None:
    """find_and_remove_max should remove all instances of biggest number from list"""
    vals = [10, 9, 8, 7, 10]
    find_and_remove_max(vals)
    assert vals == [9, 8, 7]


def test_find_and_remove_max_edge() -> None:
    """find_and_remove_max should return correct value if unconventional input"""
    vals = [1, 1, 1]
    find_and_remove_max(vals)
    assert vals == []
