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


def task_7_num_validation(num):
    try:
        return int(num)
    except ValueError:
        return 0


def task_7():
    summary = 0
    while True:
        num = task_7_num_validation(input())
        if num == 0:
            break
        summary += num
    print(summary)


if __name__ == '__main__':
    task_7()
