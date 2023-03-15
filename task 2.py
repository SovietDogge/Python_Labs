# Multiparadigm programming languages, Task 1
# Vanda Nikita Denisovich

try:
    while True:
        x = float(input())
        y = float(input())
        z = float(input())

        if y != 0 and z != 87:
            print(x + (11 - x / y) / (87 - z))
            break
        print('Incorrect value')
except ValueError:
    raise Exception('Incorrect input')
