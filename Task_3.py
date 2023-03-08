# Multiparadigm programming languages, Task 1
# Vanda Nikita Denisovich
import math

while True:
    x = float(input())
    if x == 1:
        print('Incorrect value')
    else:
        break

while True:
    a = float(input())
    if a == -2:
        print('Incorrect value')
    else:
        break

y = (x ** 3 + 2 * a * x + 3) / ((x - 1) ** 2) + (math.cos(x ** 2)) / (a + 2)
print(y)
