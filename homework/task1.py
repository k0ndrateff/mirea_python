# Реализовать простую арифметическую функцию для трёх переменных

from math import log2, ceil


def main(x, y, z):
    fst_fr_num = (96 * y - 97 * x ** 2) ** 4 + z ** 5
    fst_fr_den = 68 * log2(z) ** 6 - 63 * (ceil(y + x ** 2)) ** 5
    sec_fr_num = 40 * x ** 2 - (z ** 2 - 38 * y ** 3 - 54 * z) ** 7
    sec_fr_den = 94 * x ** 5 + 33 * log2(z - 58 * z ** 2 - 14 * y ** 3) ** 2
    fst_fr = fst_fr_num / fst_fr_den
    sec_fr = sec_fr_num / sec_fr_den
    return fst_fr - sec_fr


print(main(0.95, -0.62, 0.16))
