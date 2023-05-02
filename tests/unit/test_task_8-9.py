from unittest.mock import patch

import pytest

from task_8_9 import print_greeting, task_2, task_4, \
    task_5, task_7, task_6, make_calculations, define_color, convert_to_decimal, convert_to_binary

from utils import nums_validation, operation_validation, banknote_validation, \
    hor_coord_validation, vert_coord_validation, game_input_validation, validate_string


# should add validation to recursive output
@pytest.mark.parametrize('user_input, expected_output', [(212, 212), ('546', 546)])
def test_nums_validation(user_input, expected_output):
    user_input = nums_validation(user_input)
    assert user_input == expected_output


# should add validation to recursive output
def test_operation_validation():
    input_value = operation_validation('+')
    expected_value = '+'
    assert input_value == expected_value


# should add validation to recursive output
@pytest.mark.parametrize('input_value, expected_value', [('a', 'a')])
def test_hor_coord_validation(input_value, expected_value):
    input_value = hor_coord_validation(input_value)
    assert input_value == expected_value


# should add validation to recursive output
@pytest.mark.parametrize('input_value, expected_value', [(1, 1)])
def test_vert_coord_validation(input_value, expected_value):
    input_value = vert_coord_validation(input_value)
    assert input_value == expected_value


# should add validation to recursive output
@pytest.mark.parametrize('input_value, expected_value', [('rock', 'rock')])
def test_game_input_validation(input_value, expected_value):
    input_value = game_input_validation(input_value)
    assert input_value == expected_value


@pytest.mark.parametrize('input_value, expected_value', [('April', 'April')])
def test_validate_string(input_value, expected_value):
    input_value = validate_string(input_value)
    assert input_value == expected_value


def test_validate_string_fail():
    user_input = 'aboba'
    with pytest.raises(Exception):
        user_input = validate_string(user_input)


# should add validation to recursive output
@pytest.mark.parametrize('input_value, expected_value', [(20, 20)])
def test_banknote_validation(input_value, expected_value):
    input_value = banknote_validation(input_value)
    assert input_value == expected_value


@pytest.mark.parametrize('input_value, expected_value', [('Admin', 'Admin, I hope you are well'),
                                                         ('borov', 'borov, thank you for logging in again')])
def test_print_greeting(input_value, expected_value):
    actual = print_greeting(input_value)
    assert actual == expected_value


@pytest.mark.parametrize('input_value, expected_value', [(4, 'It is a 4-angle!'),
                                                         (12, '12 isn\'t a correct value')])
@patch('utils.nums_validation')
def test_task_2(mock_validation, input_value, expected_value):
    mock_validation.return_value = input_value
    actual = task_2(input_value)
    assert actual == expected_value


@pytest.mark.parametrize('input_value, expected_value', [(2018, '2018 is paired'), (2019, '2019 is not paired')])
@patch('utils.nums_validation')
def test_task_4(mock_validation, input_value, expected_value):
    mock_validation.return_value = input_value
    actual = task_4(input_value)
    assert actual == expected_value


@pytest.mark.parametrize('input_value, expected_value', [(2000, 'Leap year'), (2018, 'Ordinary year'),
                                                         (2004, 'Leap year')])
@patch('utils.nums_validation')
def test_task_6(mock_validation, input_value, expected_value):
    mock_validation.return_value = input_value
    actual = task_6(input_value)
    assert actual == expected_value


# want to ask some questions
# @pytest.mark.parametrize('input_value, expected_value', [(('April',), 30), (('March',), 31),
#                                                          (('February', 2000), 29), (('February', 2001), 28)])
# @patch('utils.nums_validation')
# @patch('utils.validate_string')
# @patch('task_8_9.task_6')
# def test_task_5(mock_num_val, mock_str_val, mock_task_6, input_value, expected_value):
#     month = input_value[0]
#     mock_str_val.return_value = month
#     if month != 'February':
#         actual = task_5(month)
#         assert actual == expected_value
#     year = input_value[1]
#     mock_num_val.return_value = year
#     mock_task_6.return_value =

@pytest.mark.parametrize('input_value, expected_value', [((2, 2, '+'), 4), ((2, 2, '-'), 0), ((2, 2, '/'), 1),
                                                         ((2, 2, '*'), 4), ((3, 2, 'mod'), 1),
                                                         ((45, 21, 'div'), 2), ((3, 2, 'pow'), 9)])
def test_make_calculations(input_value, expected_value):
    actual = make_calculations(input_value[0], input_value[1], input_value[2])
    assert actual == expected_value


@pytest.mark.parametrize('input_value', [(2, 0, '/'), (5, 0, 'div')])
def test_fail_make_calculations(input_value):
    with pytest.raises(Exception):
        input_value = make_calculations(input_value[0], input_value[1], input_value[2])


@pytest.mark.parametrize('input_value, expected_output', [(('a', 4), 'white'), (('a', 5), 'black'),
                                                          (('b', 2), 'black')])
def test_define_color(input_value, expected_output):
    actual = define_color(input_value[0], input_value[1])
    assert actual == expected_output


def test_convert_to_binary():
    user_input = 45
    actual = convert_to_binary(user_input)
    expected_value = '101101'
    assert actual == expected_value


def test_convert_to_decimal():
    user_input = '101101'
    actual = convert_to_decimal('101101')
    expected_output = 45
    assert actual == expected_output
