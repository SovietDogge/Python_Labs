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


task_2()
