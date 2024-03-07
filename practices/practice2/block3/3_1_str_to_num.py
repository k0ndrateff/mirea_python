# Преобразовать элементы списка s из строковой в числовую форму.


def str_to_num(s: list[str]) -> list[int]:
    return list(map(lambda x: int(x), s))


assert str_to_num([]) == []
assert str_to_num(['10']) == [10]