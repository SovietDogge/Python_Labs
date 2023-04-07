# Multiparadigm programming languages, Task 5
# Vanda Nikita Denisovich

# ex 1
from sympy import symbols

from task_7 import validate


EPS = 10 ** -4

amount = 0
n = symbols('n')
n_copy = 1

exercise = ((2 * n - 1) ** 3) / (2 ** n)

while exercise.subs('n', n_copy) > EPS:
    amount += exercise.subs('n', n_copy)
    n_copy += 1

print(f'Sum = {float(amount)}')

# ex 2

number = validate(input('Enter num: '))
power_ten = 10
count_numerals = 1

while number / power_ten > 1:
    count_numerals += 1
    power_ten *= 10

print(f'Count of numerals = {count_numerals}')

# ex 3


def find_degree(interested_num, start_num):

    correct_num = (1 / 2) * (start_num + (interested_num / start_num))
    if correct_num ** 2 == interested_num:
        return correct_num

    return find_degree(interested_num, correct_num)


power_of_num = int(input('Enter number you are interested to find his sqrt: '))
num = int(input('Enter any num: '))
print(find_degree(power_of_num, num))
