from unittest.mock import mock_open, patch, call

from task_6 import task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10

PYTHON_FEATURES = 'In Python test \n' \
                  'In Python 765\n' \
                  'In Python you can write classes'
BOOK_1 = 'Several narrative accounts of the navy of the American Revolution have been written. These usually form' \
         ' the introductory part of a history of the American Navy since 1789. The earliest of these accounts is '


def test_task_1():
    mock_op = mock_open(read_data='1\n12\n23\n54\n46\n23\n98\n32\n65\n23\n57')
    with patch('task_6.open', mock_op):
        expected = 434
        actual = task_1()

        assert actual == expected


@patch('task_6.input')
def test_task_2(mock_in):
    user_input = 22
    expected_output = [call('num_characteristic.txt', 'wt'), call().__enter__(),
                       call().write('Num 22 is paired'), call().__exit__(None, None, None)]
    mock_op = mock_open()
    with patch('task_6.open', mock_op):
        mock_in.return_value = user_input
        task_2()
        assert mock_op.mock_calls == expected_output


def test_task_3():
    mock_op = mock_open(read_data=PYTHON_FEATURES)
    with patch('task_6.open', mock_op):
        actual = task_3()
        expected_value = ['In Python you can use functions',
                          'In Python you can use OOP',
                          'In Python you can write classes']
    assert actual == expected_value


def test_task_4():
    mock_op = mock_open(read_data=PYTHON_FEATURES)
    with patch('task_6.open', mock_op):
        actual = task_4()
        expected_output = ['In C++ you can use functions',
                           'In C++ you can use OOP',
                           'In C++ you can write classes']
    assert actual == expected_output


@patch('task_6.input')
def test_task_5(mock_i):
    input_data = ['bro', '0']
    expected_data = [call('guest_book.txt', 'a'), call().__enter__(),
                     call().write('Welcome! bro\n'), call().__exit__(None, None, None)]
    mock_op = mock_open()
    with patch('task_6.open', mock_op):
        mock_i.side_effect = input_data
        task_5()
        actual = mock_op.mock_calls
    assert actual == expected_data


def test_task_6():
    mock_op = mock_open(read_data=BOOK_1)
    with patch('task_6.open', mock_op):
        actual = task_6('test_book_1.txt')
        expected = 7
    assert actual == expected


def test_task_7():
    mock_op = mock_open(read_data='test_1\ntest_2 \ntes.t_3')
    with patch('task_6.open', mock_op):
        task_7('test_t7.txt')
        actual = mock_op.mock_calls
        expected = [call('test_t7.txt', 'rt'),
                    call().__enter__(),
                    call().read(),
                    call().__exit__(None, None, None),
                    call('formatted_text.txt', 'wt'),
                    call().__enter__(),
                    call().write('test_1 test_2  tes.t_3'),
                    call().__exit__(None, None, None)]
    assert actual == expected


def test_task_8():
    mock_op = mock_open(read_data='''CHAPTER I. START IN LIFE
test
CHAPTER II. SLAVERY AND ESCAPE

CHAPTER III. WRECKED ON A DESERT ISLAND''')
    with patch('task_6.open', mock_op):
        task_8('test_t8.txt')
        actual = mock_op.mock_calls
        expected = [call('test_t8.txt', 'rt', encoding='UTF-8'),
                    call().__enter__(),
                    call().__iter__(),
                    call().__exit__(None, None, None),
                    call('chapters.txt', 'wt', encoding='UTF-8'),
                    call().__enter__(),
                    call().write('CHAPTER I. START IN LIFE\n\n'),
                    call().write('CHAPTER II. SLAVERY AND ESCAPE\n\n'),
                    call().write('CHAPTER III. WRECKED ON A DESERT ISLAND\n'),
                    call().__exit__(None, None, None)]
    assert actual == expected


def test_task_9():
    mock_op = mock_open(read_data='TEST.)1_te')
    with patch('task_6.open', mock_op):
        actual = task_9('test_t9.txt')
        expected = f'Percentage of upper letters is 14.925373134328357\n' \
                   f'Percentage of lower letters is 85.07462686567165'
    assert actual == expected


# @patch('task_6.connect')
# def test_task_10(mock_con):
#     mock_op = mock_open(read_data='''The Shawshank Redemption, 1994, 9.2
# The Godfather, 1972, 9.2
# Ratatouille, 2007, 8.0
# ''')
#     with patch('task_6.open', mock_op):
#         expected = [(1, 'The Shawshank Redemption', 1994, 9.2), (2, 'The Godfather', 1972, 9.2),
#                     (3, 'Ratatouille', 2007, 8.0),
#                     (2, 'The Godfather', 1972, 9.2), (1, 'The Shawshank Redemption', 1994, 9.2),
#                     (3, 'Ratatouille', 2007, 8.0), (2, 'The Godfather', 1972, 9.2),
#                     (1, 'The Shawshank Redemption', 1994, 9.2)]
#
#         actual = task_10()
#     assert actual == expected


def test_task_10():
    mock_op = mock_open(read_data='''test_film, 1994, 9.2
test_film_1, 1972, 9.2
Ratatouille, 2007, 8.0
''')
    with patch('task_6.connect') as mock_con:
        with patch('task_6.open', mock_op):
            task_10()
            mock_con.assert_has_calls([call().__enter__().cursor().execute(
                'CREATE TABLE IF NOT EXISTS ratings\n        (id INTEGER PRIMARY KEY,\n        title VARCHAR(20), \n   '
                '     year INT, \n        rating FLOAT)\n        '),
                call().__enter__().cursor().execute(
                    'INSERT INTO ratings (title,year,rating) values(?,?,?)',
                    ['The Shawshank Redemption', '1994', '9.2']),
                call().__enter__().commit(), call().__enter__().cursor().fetchall(),
                call().__enter__().cursor().execute(
                    'INSERT INTO ratings (title,year,rating) values(?,?,?)',
                    ['Ratatouille', '2007', '8.0']),
                call().__enter__().cursor().execute('INSERT INTO ratings (title,year,rating) values(?,?,?)',
                                                    ['The Godfather', '1972', '9.2']),
                call().__enter__().cursor().execute('SELECT * FROM ratings'),
                call().__enter__().cursor().execute(
                    'SELECT * FROM ratings\n                            WHERE rating > 8.7\n   '
                    '                         order by title'),
                call().__enter__().cursor().execute(
                    'SELECT * FROM ratings\n                                order by title')], any_order=True)
