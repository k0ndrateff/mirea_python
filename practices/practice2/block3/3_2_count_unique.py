# Подсчитать количество различных элементов в последовательности s.


def count_unique(s: list) -> int:
    return len(set(s))


assert count_unique([10, 20, 30, 40]) == 4
assert count_unique([10, 10, 10, 10]) == 1
