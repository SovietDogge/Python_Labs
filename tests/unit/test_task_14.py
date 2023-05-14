import pytest

from Task_14.my_multiset import MyMultiSet


@pytest.fixture()
def test_multiset():
    return MyMultiSet({3: 3, 1: 1, 2: 0})


@pytest.fixture()
def new_set_to_test():
    return MyMultiSet({3: 2, 2: 1, 4: 1, 1: 2})


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


@pytest.mark.parametrize('input_value', [2, 6])
def test_fail_remove(test_multiset, input_value):
    with pytest.raises(Exception):
        test_multiset.remove(input_value)


@pytest.mark.parametrize('input_value, expected_value', [(MyMultiSet(), True), (MyMultiSet({1: 1}), False)])
def test_check_empty(input_value, expected_value):
    assert input_value.check_empty() == expected_value


def test_union(test_multiset, new_set_to_test):
    actual = test_multiset.union(new_set_to_test)
    expected = {'_MyMultiSet__count_nums': {3: 3, 2: 1, 4: 1, 1: 2}}

    assert actual.__dict__ == expected


def test_intersection(test_multiset, new_set_to_test):
    actual = test_multiset.intersection(new_set_to_test)
    expected = {'_MyMultiSet__count_nums': {3: 2, 1: 1, 2: 0}}

    assert actual.__dict__ == expected
