"""tests for list utility functions"""

__author__ = "730667690"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_edge() -> None:
    """should return empty list if only odd numbers are in the list"""
    vals = [1, 3, 5, 7]
    assert only_evens(vals) == []


def test_only_evens_use_1() -> None:
    """should return all instances of an even number"""
    vals = [2, 4, 6, 4, 7]
    assert only_evens(vals) == [2, 4, 6, 4]


def test_only_evens_use_2() -> None:
    """should return even numbers even if the integers are negative"""
    vals = [-1, -2, -4, 3, 5, 6]
    assert only_evens(vals) == [-2, -4, 6]


def test_sub_edge() -> None:
    """empty list should return an empty list regardless of start and end values"""
    assert sub([], 3, 7) == []


def test_sub_use_1() -> None:
    """should return full list if start and end values match start and end of list"""
    assert sub([1, 2, 3, 4, 5], 0, 5) == [1, 2, 3, 4, 5]


def test_sub_use_2() -> None:
    """if the start value is less than 0, should start at 0"""
    assert sub([1, 2, 3, 4, 5], -2, 5) == [1, 2, 3, 4, 5]


def test_add_at_index_edge():
    """if index is negative, should raise an error"""
    vals = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(vals, 5, -2)


def test_add_at_index_use_1() -> None:
    """if index is 0, should replace first element"""
    vals = [1, 2, 3]
    add_at_index(vals, 5, 0)
    assert vals == [5, 2, 3]


def test_add_at_index_use_2() -> None:
    """if only one element in list, index 0 should replace that one element"""
    vals = [1]
    add_at_index(vals, 5, 0)
    assert vals == [5]
