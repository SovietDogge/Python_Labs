NUM_CHECK_PAIRED = 'num_characteristic.txt'


def task_1():
    amount = 0
    with open('numbers.txt', 'rt') as nums:
        for num in nums:
            amount += int(num)

    with open('amount.txt', 'wt') as file:
        file.write(str(amount))
    print(amount)


def task_2():
    try:
        num = int(input())
        if num % 2 == 0:
            with open(NUM_CHECK_PAIRED, 'wt') as check_paired_file:
                check_paired_file.write(f'Num {num} is paired')
        else:
            with open(NUM_CHECK_PAIRED, 'wt') as check_paired_file:
                check_paired_file.write(f'Num {num} is not paired')

    except ValueError:
        print('It must be a number')


def task_3():
    python_features = []
    with open('learning_python.txt', 'rt') as file:
        for line in file:
            python_features.append(line)
    print(python_features)


def task_4():
    python_features = []
    with open('learning_python.txt', 'rt') as file:
        for line in file:
            line = line.replace('Python', 'C++')
            python_features.append(line)
    print(python_features)


task_4()
