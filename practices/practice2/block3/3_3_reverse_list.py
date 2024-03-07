# Обратить последовательность s без использования функций.


def reverse_list(s: list) -> list:
    return s[::-1]


assert reverse_list([1, 2, 3]) == [3, 2, 1]
assert reverse_list([1, 4, 2, 5]) == [5, 2, 4, 1]
