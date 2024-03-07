# Выдать список индексов, на которых найден элемент x в последовательности s.


def index_of(s: list, x: any) -> list[int]:
    return [i for i, x in enumerate(s) if x == x]


assert index_of([10, 12, 54, 12], 12) == [1, 3]
assert index_of([12, 12, 12, 12], 10) == []
