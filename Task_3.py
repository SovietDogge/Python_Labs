# Multiparadigm programming languages, Task 1
# Vanda Nikita Denisovich
import math
TEMPLATE = 'Incorrect value'

try:

    while True:
        x = float(input())
        a = float(input())
        if x == 1 or a == -2:
            print(TEMPLATE)
        else:
            break
except ValueError:
    print('Incorrect input')

    y = (x ** 3 + 2 * a * x + 3) / ((x - 1) ** 2) + (math.cos(x ** 2)) / (a + 2)
    print(y)
