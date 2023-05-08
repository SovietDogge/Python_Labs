import random

from validations import nums_validation, vert_coord_validation, validation_pattern

EMPTY_USERS_WARNING = 'We need to add some users!!!'
POSSIBLE_OPERATOR = ['+', '-', '/', '*', 'mod', 'pow', 'div']
POSSIBLE_BANKNOTES = {1: 'Vladimir Velikiy', 2: 'Yroslav Mudryi', 5: 'Bogda Hmelnitzkyi',
                      10: 'Ivan Mazepa', 20: 'Ivan Franko', 50: 'Mihail Grushevskyi',
                      100: 'Taras Shevchenko', 200: 'Lesy Ukrainka', 500: 'Grigoriy Skovoroda',
                      1000: 'Vladimir Vernadskyi'}
POSSIBLE_COORDINATES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
POSSIBLE_VARIANTS = ['rock', 'paper', 'scissors']


def print_greeting(name):
    if name == 'Admin':
        return 'Admin, I hope you are well'
    return f'{name}, thank you for logging in again'


def task_1(users):
    if len(users) != 0:
        for user in users:
            print(print_greeting(user))
    else:
        print(EMPTY_USERS_WARNING)


def task_2(sides_count):
    sides_count = nums_validation(sides_count)
    for i in range(3, 7):
        if i == sides_count:
            return f'It is a {i}-angle!'
    return f"{sides_count} isn't a correct value"


def task_3():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in nums:
        if num == 1:
            print(f'{num}-st')
        elif num in (2, 3):
            print(f'{num}-nd')
        else:
            print(f'{num}-th')


def task_4(user_input_year):
    num = nums_validation(user_input_year)
    if num % 2 == 0.:
        return f'{num} is paired'
    return f'{num} is not paired'


def task_6(year):
    year = nums_validation(year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 'Leap'
    return 'Ordinary'


def define_nom_of_days():
    year = nums_validation(input('Enter year: '))
    year_type = task_6(year)
    return 29 if year_type == 'Leap' else 28


def task_5(users_month):
    months = {'January': 31, 'March': 31, 'May': 31, 'July': 31,
              'August': 31, 'October': 31, 'December': 31, 'April': 30, 'June': 30,
              'September': 30, 'November': 30}
    users_month = validation_pattern(users_month, months.keys())
    return months[users_month] if users_month != 'February' else define_nom_of_days()


def task_7():
    summary = 0
    while True:
        num = nums_validation(input())
        if num == 0:
            break
        summary += num
    return summary


def make_calculations(number1, number2, oper):
    if oper == '+':
        return number1 + number2
    if oper == '-':
        return number1 - number2
    if oper == '/':
        try:
            return number1 / number2
        except ZeroDivisionError:
            raise Exception('You can\'t divide by zero')
    if oper == '*':
        return number1 * number2
    if oper == 'mod':
        return number1 % number2
    if oper == 'div':
        try:
            return number1 // number2
        except ZeroDivisionError:
            raise Exception('You can\'t divide by zero')
    if oper == 'pow':
        return number1 ** number2


def task_8():
    num1 = nums_validation(input('Enter first num '))
    num2 = nums_validation(input('Enter second num '))
    operation = validation_pattern(input('Enter operation '), POSSIBLE_OPERATOR)
    return f'Result = {make_calculations(num1, num2, operation)}'


def task_9(value):
    value = validation_pattern(value, POSSIBLE_BANKNOTES.keys())
    return POSSIBLE_BANKNOTES[value]


def define_color(horizon_cor, vertical_cor):
    if (horizon_cor in 'aceg' and vertical_cor % 2 == 1) or \
            (horizon_cor in 'bdfh' and vertical_cor % 2 == 0):
        return 'black'
    return 'white'


def task_10():
    hor_coord = validation_pattern(input('Enter horizontal coordinate '), POSSIBLE_COORDINATES)
    vert_coord = vert_coord_validation(input('Enter vertical coordinate '))
    result = define_color(hor_coord, vert_coord)
    return f'field is {result}'


def convert_to_binary(number):
    result = ''
    while number > 0:
        r = number % 2
        result = str(r) + result
        number = int(number / 2)
    return result


def convert_to_decimal(number):
    degree = len(str(number)) - 1
    new_num = 0
    i = 0
    while degree >= 0:
        if number[i] == '1':
            new_num += 2 ** degree
        degree -= 1
        i += 1

    return new_num


def task_11():
    num = nums_validation(input('Enter any num '))
    binary_num = convert_to_binary(num)
    decimal_num = convert_to_decimal(binary_num)
    return f'Number {num} in binary = {binary_num}, in Decimal = {decimal_num}'


def task_12():
    user_choice = validation_pattern(input('Enter rock, paper or scissors '), POSSIBLE_VARIANTS)

    bot_choice = random.choice(POSSIBLE_VARIANTS)
    victory_condition = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    print(f'Bot choose {bot_choice}')

    if user_choice == bot_choice:
        return 'Draw'
    result = 'Victory' if victory_condition[user_choice] == bot_choice else 'Defeat'
    return result


if __name__ == '__main__':
    print(task_12())
