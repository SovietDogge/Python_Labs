from unittest.mock import patch

import pytest

from task_8_9 import print_greeting, task_2, task_4, \
    task_5, task_7, task_6, make_calculations, define_color, convert_to_decimal, convert_to_binary, POSSIBLE_BANKNOTES, \
    POSSIBLE_VARIANTS, POSSIBLE_OPERATOR, POSSIBLE_COORDINATES, define_nom_of_days, task_12

from validations import nums_validation, vert_coord_validation, validation_pattern

MONTHS = ['February',
          'January', 'March', 'May', 'July',
          'August', 'October', 'December', 'April', 'June',
          'September', 'November']


# should add validation to recursive output
@pytest.mark.parametrize('user_input, expected_output', [('fdndn', 10), (212, 212), ('546', 546)])
@patch('validations.nums_validation', return_value=10)
@patch('validations.input')
def test_nums_validation(mock_v, mock_i, user_input, expected_output):
    actual = nums_validation(user_input)
    assert actual == expected_output


@pytest.mark.parametrize('input_value, expected_value', [(1, 1), (21, 20)])
@patch('validations.validation_pattern', return_value=20)
@patch('validations.input')
def test_validation_pattern_banknotes(mock_v, mock_i, input_value, expected_value):
    possible_value = POSSIBLE_BANKNOTES.keys()
    actual = validation_pattern(input_value, possible_value)
    assert actual == expected_value


@pytest.mark.parametrize('input_value, expected_value, possible_value', [('paper', 'paper', POSSIBLE_VARIANTS),
                                                                         ('gork', 'rock', POSSIBLE_VARIANTS)])
@patch('validations.validation_pattern', return_value='rock')
@patch('validations.input')
def test_val_pattern_game_var(mock_v, mock_i, input_value, expected_value, possible_value):
    actual = validation_pattern(input_value, possible_value)
    assert actual == expected_value


@pytest.mark.parametrize('input_value, expected_value, possible_value', [('a', 'a', POSSIBLE_COORDINATES),
                                                                         ('ba', 'b', POSSIBLE_COORDINATES)])
@patch('validations.validation_pattern', return_value='b')
@patch('validations.input')
def test_val_pattern_coord(mock_v, mock_i, input_value, expected_value, possible_value):
    actual = validation_pattern(input_value, possible_value)
    assert actual == expected_value


@pytest.mark.parametrize('input_value, expected_value, possible_value', [('+', '+', POSSIBLE_OPERATOR),
                                                                         ('///', '//', POSSIBLE_OPERATOR)])
@patch('validations.validation_pattern', return_value='//')
@patch('validations.input')
def test_val_pattern_coord(mock_v, mock_i, input_value, expected_value, possible_value):
    actual = validation_pattern(input_value, possible_value)
    assert actual == expected_value


@pytest.mark.parametrize('input_value, expected_value', [('April', 'April'),
                                                         ('Actober', 'October')])
@patch('validations.validation_pattern', return_value='October')
@patch('validations.input')
def test_val_pattern_month(mock_v, mock_i, input_value, expected_value):
    actual = validation_pattern(input_value, MONTHS)
    assert actual == expected_value


@pytest.mark.parametrize('input_value, expected_value', [(1, 1), (9, 1), ('word', 1)])
@patch('validations.vert_coord_validation', return_value=1)
@patch('validations.input')
def test_vert_coord_validation(mock_v, mock_i, input_value, expected_value):
    actual = vert_coord_validation(input_value)
    assert actual == expected_value


@pytest.mark.parametrize('input_value, expected_value', [('Admin', 'Admin, I hope you are well'),
                                                         ('borov', 'borov, thank you for logging in again')])
def test_print_greeting(input_value, expected_value):
    actual = print_greeting(input_value)
    assert actual == expected_value


@pytest.mark.parametrize('input_value, expected_value', [(4, 'It is a 4-angle!'),
                                                         (12, '12 isn\'t a correct value')])
@patch('task_8_9.nums_validation')
def test_task_2(mock_validation, input_value, expected_value):
    mock_validation.return_value = input_value
    actual = task_2(input_value)
    assert actual == expected_value


@pytest.mark.parametrize('input_value, expected_value', [(2018, '2018 is paired'), (2019, '2019 is not paired')])
@patch('task_8_9.nums_validation')
def test_task_4(mock_v, input_value, expected_value):
    mock_v.return_value = input_value
    actual = task_4(input_value)
    assert actual == expected_value


@pytest.mark.parametrize('input_value, expected_value', [(2000, 'Leap'), (2018, 'Ordinary'),
                                                         (2004, 'Leap')])
@patch('task_8_9.nums_validation')
def test_task_6(mock_val, input_value, expected_value):
    mock_val.return_value = input_value
    actual = task_6(input_value)
    assert actual == expected_value


@pytest.mark.parametrize('expected_value, input_year', [(29, (2000, 'Leap')), (28, (2001, 'Ordinary'))])
@patch('task_8_9.nums_validation')
@patch('task_8_9.input')
@patch('task_8_9.task_6')
def test_define_nom_of_days(mock_t6, mock_in, mock_val, expected_value, input_year):
    mock_val.return_value = input_year[0]
    mock_t6.return_value = input_year[1]
    actual = define_nom_of_days()
    assert actual == expected_value


@pytest.mark.parametrize('input_value, expected_value', [('April', 30), ('February', 29), ('February', 28)])
@patch('task_8_9.define_nom_of_days')
@patch('task_8_9.validation_pattern')
def test_task_5(mock_val, mock_def, input_value, expected_value):
    mock_val.return_value = input_value
    mock_def.return_value = expected_value
    actual = task_5(input_value)
    assert actual == expected_value


@pytest.mark.parametrize('first_num, second_num, operator, expected_value',
                         [(2, 2, '+', 4), (2, 2, '-', 0), (2, 2, '/', 1),
                          (2, 2, '*', 4), (3, 2, 'mod', 1),
                          (45, 21, 'div', 2), (3, 2, 'pow', 9),
                          (2, 0, '/', None), (5, 0, 'div', None)])
def test_make_calculations(first_num, second_num, operator, expected_value):
    actual = make_calculations(first_num, second_num, operator)
    assert actual == expected_value


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
    actual = convert_to_decimal(user_input)
    expected_output = 45
    assert actual == expected_output


@patch('task_8_9.nums_validation', side_effect=[10, 0])
@patch('task_8_9.input')
def test_task_7(v_mock, i_mock):
    actual = task_7()
    expected = 10
    assert actual == expected


@pytest.mark.parametrize('expected_output, bot_choice',
                         [('Victory', 'scissors'), ('Draw', 'rock'), ('Defeat', 'paper')])
@patch('task_8_9.validation_pattern', return_value='rock')
@patch('task_8_9.input')
@patch('task_8_9.random.choice')
def test_task_12(rd_mock, mock_i, val_mock, expected_output, bot_choice):
    rd_mock.return_value = bot_choice
    actual = task_12()
    assert actual == expected_output
