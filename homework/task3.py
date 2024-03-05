# Реализовать итерационную функцию

def main(a, m, z):
    outer_sum = 0
    for k in range(1, m + 1):
        inner_sum = 0
        for j in range(1, a + 1):
            inner_sum += ((66 - z ** 2) ** 2 - (1 + 67 * j ** 2) ** 6 -
                          6 * k ** 5)
        outer_sum += inner_sum
    return outer_sum
