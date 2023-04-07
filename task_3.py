# Multiparadigm programming languages, Task 3
# Vanda Nikita Denisovich
import math

try:

    while True:
        x = float(input())
        a = float(input())
        if x == 1 or a == -2:
            print('Incorrect value')
        else:
            y = (x ** 3 + 2 * a * x + 3) / ((x - 1) ** 2) + (math.cos(x ** 2)) / (a + 2)
            print(y)
            break
except ValueError:
    print('Incorrect input')
