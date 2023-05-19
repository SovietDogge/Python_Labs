from unittest.mock import mock_open, patch

from task_11 import task_1, task_2, task_3

DATES = '20.12.2000,test 2001/02/01 test test test 2003/1/17. test 12.4.2004, 8.8.2008'
SENTENCES = 'Test sentence. Another test? Final test! fail test'
EVENTS = 'Test 1996. Test.'


def test_task_1():
    mock_op = mock_open(read_data=DATES)
    with patch('task_11.open', mock_op):
        user_input = 'dates.txt'
        actual = task_1(user_input)
    expected_value = ['20.12.2000', '12.04.2004', '08.08.2008', '01.02.2001', '17.01.2003']

    assert actual == expected_value


def test_task_2():
    mock_op = mock_open(read_data=SENTENCES)
    with patch('task_11.open', mock_op):
        user_input = 'some_text.txt'
        actual = task_2(user_input)
    expected_value = ['Test sentence.', 'Another test?', 'Final test!']

    assert expected_value == actual


def test_task_3():
    mock_op = mock_open(read_data=EVENTS)
    with patch('task_11.open', mock_op):
        user_input = 'events.txt'
        actual = task_3(user_input)
    expected_value = {'1996': 'Test 1996.'}

    assert actual == expected_value
