# Multiparadigm programming languages, Task 5
# Vanda Nikita Denisovich
from sympy import symbols

EPS = 10 ** -4


def nums_validation(num):
    try:
        return int(num)
    except ValueError:
        print('Incorrect input')
        return nums_validation(input())


def find_sum():
    amount = 0
    n = symbols('n')
    n_copy = 1

    exercise = ((2 * n - 1) ** 3) / (2 ** n)

    while exercise.subs('n', n_copy) > EPS:
        amount += exercise.subs('n', n_copy)
        n_copy += 1

    return f'Sum = {round(float(amount), 4)}'


def find_power_10(number):
    power_ten = 10
    count_numerals = 1

    while number // power_ten:
        count_numerals += 1
        power_ten *= 10

    print(f'Count of numerals = {count_numerals}')
    return count_numerals


def find_degree(interested_num, start_num):
    correct_num = (1 / 2) * (start_num + (interested_num / start_num))

    if abs(start_num - correct_num) < EPS * start_num:
        return round(correct_num, 4)

    return find_degree(interested_num, correct_num)


if __name__ == '__main__':
    power_of_num = nums_validation(input('Enter number you are interested to find his sqrt: '))
    num = nums_validation(input('Enter any num: '))
    print(find_degree(power_of_num, num))
    print(find_sum())
