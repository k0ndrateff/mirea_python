# Реализуйте функцию fast_mul в соответствии с алгоритмом
# двоичного умножения в столбик (без рекурсии!).
# Добавьте автоматическое тестирование, как в случае с naive_mul.

import random


def fast_mul(x: int, y: int) -> int:
    x_array = [x]
    y_array = [y]
    res_array = []

    while x > 1:
        x //= 2
        y *= 2
        x_array.append(x)
        y_array.append(y)

    for i in range(len(x_array)):
        if x_array[i] % 2 != 0:
            res_array.append(y_array[i])

    return sum(res_array)


assert fast_mul(10, 15) == 10 * 15

a = random.randint(1, 1000)
b = random.randint(1, 1000)
assert fast_mul(a, b) == a * b
