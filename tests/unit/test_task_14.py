import pytest

from Task_14.my_multiset import MyMultiSet


def test_clear():
    input_value = MyMultiSet()
    input_value.add_num(3)

    expected_value = in