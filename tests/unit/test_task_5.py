import pytest
from Task_5 import find_power_10, find_degree


@pytest.mark.parametrize('input_number, expected_number', [(23, 2), (100, 3)])
def test_find_power_10(input_number, expected_number):
    actual = find_power_10(input_number)
    assert actual == expected_number


@pytest.mark.parametrize('interested_num, start_num, result',
                         [(65, 17, 'Limit of recursion achieved'), (9, 3, 3)])
def test_find_degree(interested_num, start_num, result):
    actual = find_degree(interested_num, start_num)
    assert actual == result
