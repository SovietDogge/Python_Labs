import pytest
from Task_5 import find_power_10, find_degree, find_sum


@pytest.mark.parametrize('input_number, expected_number', [(23, 2), (100, 3)])
def test_find_power_10(input_number, expected_number):
    actual = find_power_10(input_number)
    assert actual == expected_number


@pytest.mark.parametrize('interested_num, start_num, result', [(45, 34, 6.7082)])
def test_find_degree(interested_num, start_num, result):
    actual = find_degree(interested_num, start_num)
    assert actual == result


def test_find_sum():
    expected_num = 146.9999
    actual = find_sum()
    assert f'Sum = {expected_num}' == actual
