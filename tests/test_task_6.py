from unittest.mock import mock_open, patch, call

import pytest

from task_6 import task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10

PYTHON_FEATURES = 'In Python you can use functions' \
                  'In Python you can use OOP' \
                  'In Python you can write classes'


def test_task_1():
    mock_op = mock_open(read_data='1\n12\n23\n54\n46\n23\n98\n32\n65\n23\n57')
    with patch('task_6.open', mock_op):
        expected = 434
        actual = task_1()
        print(mock_op.mock_calls)

        assert actual == expected


@patch('task_6.input')
@pytest.mark.parametrize('user_input, expected_output',
                         [(22, [call('num_characteristic.txt', 'wt'), call().__enter__(),
                                call().write('Num 22 is paired'), call().__exit__(None, None, None)])])
def test_task_2(mock_in, user_input, expected_output):
    mock_op = mock_open()
    with patch('task_6.open', mock_op):
        mock_in.return_value = user_input
        task_2()

        assert mock_op.mock_calls == expected_output


@patch('task_6.open')
def test_task_3(mock_op):
    mock_op = mock_open(mock_op, read_data=PYTHON_FEATURES)
    actual = task_3()
    expected_value = PYTHON_FEATURES
    assert actual == expected_value
