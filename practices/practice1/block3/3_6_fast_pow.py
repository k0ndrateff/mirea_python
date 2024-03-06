# Реализуйте аналогичную функцию fast_pow для возведения в степень.
# Решение необходимо получить только с помощью небольших модификаций
# предыдущего решения.
import math
import random


def fast_pow(x: int, y: int) -> int:
    x_array = [x]
    y_array = []
    result = 1

    while y > 1:
        if y % 2 != 0:
            y_array.append(x)
        x *= x
        x_array.append(x)
        y //= 2

    for i in range(len(y_array)):
        if i == 0:
            result = y_array[i]
        else:
            result *= y_array[i]

    return result

print(fast_pow(10, 2))

assert fast_pow(10, 15) == 10 * 15

a = random.randint(1, 1000)
b = random.randint(1, 1000)
assert fast_pow(a, b) == a * b