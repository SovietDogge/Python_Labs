# Multiparadigm programming languages, Task 1
# Vanda Nikita Denisovich

try:

    while True:
        x = float(input())
        y = float(input())
        z = float(input())
        if y == 0 or z == 87:
            print('Incorrect value')
        else:
            break

except ValueError:
    print('Incorrect input')

print(x + (11 - x / y) / (87 - z))
