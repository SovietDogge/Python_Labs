import pytest

from Task_14.my_multiset import MyMultiSet


def test_clear():
    input_value = MyMultiSet()
    expected_value = {'_MyMultiSet__count_nums': {}}
    assert input_value.__dict__ == expected_value
