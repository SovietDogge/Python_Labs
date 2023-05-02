INCORRECT_INPUT_ER = 'Incorrect input'
ENTER_CORRECT_NUM = 'Please enter num from 0 to 8: '


def nums_validation(num):
    try:
        return int(num)
    except ValueError:
        print(INCORRECT_INPUT_ER)
        return nums_validation(input())


def operation_validation(oper):
    possible_operations = ['+', '-', '/', '*', 'mod', 'pow', 'div']
    if oper in possible_operations:
        return oper
    print('Write correct operation')
    return operation_validation(input())


def banknote_validation(value):
    possible_values = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    if value in possible_values:
        return value
    print(INCORRECT_INPUT_ER)
    return banknote_validation(int(input()))


def hor_coord_validation(coordinate):
    possible_coordinates = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    if coordinate in possible_coordinates:
        return coordinate
    print(INCORRECT_INPUT_ER)
    return hor_coord_validation(input('Please enter another letter: '))


def vert_coord_validation(coordinate):
    try:
        coordinate = int(coordinate)
        if 0 < coordinate <= 8:
            return coordinate
        print(INCORRECT_INPUT_ER)
        return vert_coord_validation(int(input(ENTER_CORRECT_NUM)))
    except ValueError:
        return vert_coord_validation(int(input(ENTER_CORRECT_NUM)))


def game_input_validation(value):
    possible_variants = ['rock', 'paper', 'scissors']
    if value in possible_variants:
        return value
    print(INCORRECT_INPUT_ER)
    return game_input_validation(input('Please, enter rock, paper or scissors '))


def validate_string(value):
    months = ['April', 'June', 'September', 'November',
              'January', 'March', 'May', 'July', 'August',
              'October', 'December', 'February']
    if value not in months:
        return Exception('Enter a correct title of month')
    return value
