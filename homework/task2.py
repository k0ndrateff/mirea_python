# Реализовать кусочную функцию

from math import floor, atan


def main(y):
    if y < 38:
        return 6 * y ** 4 + y
    elif y < 123:
        return ((y ** 2) / 4) ** 6 + 42 * floor(y) ** 5 + (y ** 4) / 47
    elif y < 179:
        return y ** 3
    elif y < 218:
        return (33 * atan(53 * y ** 2 - y ** 3 - y / 66) ** 6 +
                (80 * y) ** 5 / 93)
    else:
        return 13 * y ** 2 - 1
