from unittest.mock import mock_open, patch, call

from task_6 import task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10

PYTHON_FEATURES = 'In Python test\n' \
                  'In Python 765\n'
CHAPTERS = '''CHAPTER I. START IN LIFE
test
CHAPTER II. SLAVERY AND ESCAPE
test 1324
CHAPTER III. WRECKED ON A DESERT ISLAND'''


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
        expected_value = ['In Python test',
                          'In Python 765']
    assert actual == expected_value


def test_task_4():
    mock_op = mock_open(read_data=PYTHON_FEATURES)
    with patch('task_6.open', mock_op):
        actual = task_4()
        expected_output = ['In C++ test',
                           'In C++ 765']
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
    mock_op = mock_open(read_data='theTest123 /.@text THE')
    with patch('task_6.open', mock_op):
        actual = task_6('test_book_1.txt')
        expected = 2
    assert actual == expected


def test_task_7():
    mock_op = mock_open(read_data='test_1\ntest_2 \ntes.t_3')
    with patch('task_6.open', mock_op):
        task_7('test_t7.txt')
        mock_op.assert_has_calls([call('test_t7.txt', 'rt'),
                                  call('formatted_text.txt', 'wt'),
                                  call().write('test_1 test_2  tes.t_3')])


def test_task_8():
    mock_op = mock_open(read_data=CHAPTERS)
    with patch('task_6.open', mock_op):
        task_8('test_t8.txt')
        mock_op.assert_has_calls([call().write('CHAPTER I. START IN LIFE\n\n'),
                                  call().write('CHAPTER II. SLAVERY AND ESCAPE\n\n'),
                                  call().write('CHAPTER III. WRECKED ON A DESERT ISLAND\n')])


def test_task_9():
    mock_op = mock_open(read_data='TEST.)1_te')
    with patch('task_6.open', mock_op):
        actual = task_9('test_t9.txt')
        expected = f'Percentage of upper letters is 66.66666666666666\n' \
                   f'Percentage of lower letters is 33.33333333333334'
    assert actual == expected


def test_task_10():
    mock_op = mock_open(read_data='''test_film, 1994, 9.2
test_film_1, 1972, 9.2
test_film_2, 2007, 8.0
''')
    with patch('task_6.connect') as mock_con:
        with patch('task_6.open', mock_op):
            task_10()
            cr = call().__enter__().cursor()
            mock_con.assert_has_calls([
                cr.execute(
                    'INSERT INTO ratings (title,year,rating) values(?,?,?)',
                    ['test_film', '1994', '9.2']),
                cr.execute(
                    'INSERT INTO ratings (title,year,rating) values(?,?,?)',
                    ['test_film_2', '2007', '8.0']),
                cr.execute('INSERT INTO ratings (title,year,rating) values(?,?,?)',
                                                    ['test_film_1', '1972', '9.2'])], any_order=True)
