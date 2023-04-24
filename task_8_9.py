import random

from utils import *

EMPTY_USERS_WARNING = 'We need to add some users!!!'


def validate_num(value):
    try:
        return float(value)
    except ValueError:
        raise Exception(f'Incorrect value - {value}')


def validate_string(value):
    months = ['April', 'June', 'September', 'November',
              'January', 'March', 'May', 'July', 'August',
              'October', 'December', 'February']
    if value not in months:
        raise Exception('Enter a correct title of month')


def print_greeting(name):
    if name == 'Admin':
        return 'Admin, I hope you are well'
    return f'{name}, thank you for logging in again'


def task_1():
    users = ['Admin', 'aboba', 'Nikita', 'Valera', 'borov']
    if len(users) != 0:
        for user in users:
            print(print_greeting(user))
    else:
        print(EMPTY_USERS_WARNING)

    users.clear()
    if len(users) != 0:
        for user in users:
            print_greeting(user)
    else:
        print(EMPTY_USERS_WARNING)


def task_2(sides_count):
    validate_num(sides_count)
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


def task_4():
    num = validate_num(input())
    if num % 2 == 0.:
        print(f'{num} is paired')
    else:
        print(f'{num} is not paired')


def task_6(year):
    validate_num(year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 'Leap year'
    return 'Ordinary year'


def task_5(users_month):
    validate_string(users_month)
    month_30_day = ['April', 'June', 'September', 'November']
    month_31_day = ['January', 'March', 'May', 'July', 'August', 'October', 'December']

    if users_month in month_30_day:
        print(f'{users_month} has 30')
    elif users_month in month_31_day:
        print(f'{users_month} has 31')
    else:
        year = validate_num(input('Enter year: '))
        year_type = task_6(year)
        if year_type == 'Leap year':
            print(f'{users_month} has 29 in a leap year')
        else:
            print(f'{users_month} has 28 in an ordinary year')


def task_7():
    summary = 0
    while True:
        num = nums_validation(input())
        if num == 0:
            break
        summary += num
    print(summary)


def make_calculations(number1, number2, oper):
    if oper == '+':
        return number1 + number2
    elif oper == '-':
        return number1 - number2
    elif oper == '/':
        try:
            return number1 / number2
        except ZeroDivisionError:
            raise Exception('You can\'t divide by zero')
    elif oper == '*':
        return number1 * number2
    elif oper == 'mod':
        return number1 % number2
    elif oper == 'div':
        try:
            return number1 // number2
        except ZeroDivisionError:
            raise Exception('You can\'t divide by zero')
    elif oper == 'pow':
        return number1 ** number2


def task_8():
    num1 = nums_validation(input('Enter first num '))
    num2 = nums_validation(input('Enter second num '))
    operation = operation_validation(input('Enter operation '))
    print(f'Result = {make_calculations(num1, num2, operation)}')


def find_banknote_info(value):
    possible_banknotes = {1: 'Vladimir Velikiy', 2: 'Yroslav Mudryi', 5: 'Bogda Hmelnitzkyi',
                          10: 'Ivan Mazepa', 20: 'Ivan Franko', 50: 'Mihail Grushevskyi',
                          100: 'Taras Shevchenko', 200: 'Lesy Ukrainka', 500: 'Grigoriy Skovoroda',
                          1000: 'Vladimir Vernadskyi'}
    return possible_banknotes[value], value


def task_9():
    banknote_value = banknote_validation(int(input('Enter a banknote value ')))
    result = find_banknote_info(banknote_value)
    print(f'Value {result[1]} is {result[0]}')


def define_color(horizon_cor, vertical_cor):
    if horizon_cor in 'aceg' and vertical_cor % 2 == 1:
        return 'black'
    elif horizon_cor in 'bdfh' and vertical_cor % 2 == 0:
        return 'black'
    else:
        return 'white'


def task_10():
    hor_coord = hor_coord_validation(input('Enter horizontal coordinate '))
    vert_coord = vert_coord_validation(input('Enter vertical coordinate '))
    result = define_color(hor_coord, vert_coord)
    print(f'field is {result}')


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
    print(f'Number {num} in binary = {binary_num}, in Decimal = {decimal_num}')


def task_12():
    user_choice = game_input_validation(input('Enter rock, paper or scissors '))
    possible_variants = ['rock', 'paper', 'scissors']
    bot_choice = random.sample(possible_variants, 1)[0]
    victory_condition = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    print(f'Bot choose {bot_choice}')

    if user_choice == bot_choice:
        return 'draw'
    elif victory_condition[user_choice] == bot_choice:
        return 'Victory'
    return 'Defeat'


if __name__ == '__main__':
    while True:
        print(task_12())
