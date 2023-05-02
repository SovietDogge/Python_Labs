import pytest

from task_8_9 import print_greeting, task_2, task_4,\
    task_5, task_7, task_6

from utils import nums_validation, operation_validation, banknote_validation,\
    hor_coord_validation, vert_coord_validation, game_input_validation, validate_string


@pytest.mark.pametrize('user_input, expected_output', ((212, 212), ('546', 546)))
def test_nums_validation(user_input, expected_output):
    user_input = nums_validation(user_input)
    assert user_input == expected_output


@pytest.mark.xfail()
def test_fail_nums_validation(user_input, expected_output):
    user_input = 'sdsvd'
    assert nums_validation(user_input)
