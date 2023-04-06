# Multiparadigm programming languages, Task 5
# Vanda Nikita Denisovich
from sympy import *

EPS = 10 ** -4
LIMIT_RECURSION = 100


def find_sum():
    amount = 0
    n = symbols('n')
    n_copy = 1

    exercise = ((2 * n - 1) ** 3) / (2 ** n)

    while exercise.subs('n', n_copy) > EPS:
        amount += exercise.subs('n', n_copy)
        n_copy += 1

    print(f'Sum = {float(amount)}')


def find_power_10(number):
    power_ten = 10
    count_numerals = 1

    while number // power_ten:
        count_numerals += 1
        power_ten *= 10

    print(f'Count of numerals = {count_numerals}')
    return count_numerals


def find_degree(interested_num, start_num, current_recursion=0):
    if current_recursion < LIMIT_RECURSION:
        current_recursion += 1
        correct_num = (1 / 2) * (start_num + (interested_num / start_num))
        if correct_num ** 2 == interested_num:
            return correct_num
        current_recursion += 1
        return find_degree(interested_num, correct_num, current_recursion)
    return 'Limit of recursion achieved'


if __name__ == '__main__':
    power_of_num = int(input('Enter number you are interested to find his sqrt: '))
    num = int(input('Enter any num: '))
    print(find_degree(power_of_num, num))
