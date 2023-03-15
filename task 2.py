# Multiparadigm programming languages, Task 1
# Vanda Nikita Denisovich
INCORRECT_MESSAGE = 'Incorrect input'

try:
    while True:
        x = float(input())
        y = float(input())
        z = float(input())

        if y != 0 and z != 87:
            print(x + (11 - x / y) / (87 - z))
            break
        print(INCORRECT_MESSAGE)
except ValueError:
    print(INCORRECT_MESSAGE)
