def task_1():
    amount = 0
    with open('numbers.txt', 'rt') as nums:
        for num in nums:
            amount += int(num)

    with open('amount.txt', 'wt') as file:
        file.write(str(amount))
    print(amount)


task_1()
