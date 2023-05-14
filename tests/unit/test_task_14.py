import pytest

from Task_14.my_multiset import MyMultiSet


@pytest.fixture()
def test_multiset():
    return MyMultiSet({3: 3, 1: 1, 2: 0})


def test_clear(test_multiset):
    test_multiset.clear()
    expected_value = {'_MyMultiSet__count_nums': {}}

    assert test_multiset.__dict__ == expected_value


def test_add_num(test_multiset):
    test_multiset.add_num(3)
    expected_output = {'_MyMultiSet__count_nums': {3: 4, 1: 1, 2: 0}}

    assert test_multiset.__dict__ == expected_output


@pytest.mark.parametrize('input_value, expected_value', [(3, 3), (4, None)])
def test_get_count(input_value, expected_value, test_multiset):

    assert test_multiset.get_count(input_value) == expected_value


def test_count_nums(test_multiset):
    expected_value = {3: 3, 1: 1, 2: 0}

    assert test_multiset.count_nums == expected_value


def test_setter_count_nums(test_multiset):
    new_value = {1: 2, 4: 5}
    test_multiset.count_nums = new_value
    expected_value = {'_MyMultiSet__count_nums': {1: 2, 4: 5}}

    assert test_multiset.__dict__ == expected_value


def test_remove(test_multiset):
    input_value = 3
    test_multiset.remove(input_value)
    expected_value = {'_MyMultiSet__count_nums': {3: 2, 1: 1, 2: 0}}

    assert test_multiset.__dict__ == expected_value


def test_fail_remove(test_multiset):
    pass