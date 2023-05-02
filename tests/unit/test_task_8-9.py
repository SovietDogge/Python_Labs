import pytest

from task_8_9 import print_greeting, task_2, task_4,\
    task_5, task_7, task_6

from utils import nums_validation, operation_validation, banknote_validation,\
    hor_coord_validation, vert_coord_validation, game_input_validation, validate_string


# should add validation to recursive output
@pytest.mark.parametrize('user_input, expected_output', [(212, 212), ('546', 546)])
def test_nums_validation(user_input, expected_output):
    user_input = nums_validation(user_input)
    assert user_input == expected_output


@pytest.mark.xfail()
def test_fail_nums_validation():
    user_input = 'sdsvd'
    assert nums_validation(user_input)


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


@pytest.mark.parametrize('input_value, expected_value', [('April', 'April'),
                                                         ('aboba', Exception('Enter a correct title of month'))])
def test_validate_string(input_value, expected_value):
    input_value = validate_string(input_value)
    assert input_value == expected_value
