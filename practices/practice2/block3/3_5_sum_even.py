# Сложить элементы списка s с четными индексами.


def sum_even_indices(s: list[int]) -> int:
    return sum(s[::2])


assert sum_even_indices([1, 10, 1, 10, 1, 10]) == 3
assert sum_even_indices([10, 1, 10, 1, 10, 1]) == 30