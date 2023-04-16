EMPTY_USERS_WARNING = 'We need to add some users!!!'


def print_greeting(name):
    if name == 'Admin':
        return 'Admin, I hope you are well'
    else:
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
    for i in range(3, 7):
        if i == sides_count:
            return f'It is a {i}-angle!'
    return f"{sides_count} isn't correct value"


if __name__ == '__main__':
    task_1()
