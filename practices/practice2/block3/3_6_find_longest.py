# Найти строку максимальной длины в списке строк s.


def longest(s: list[str]) -> str:
    return max(set(s), key=len)


assert longest(["long", "lolololong", "smol"]) == "lolololong"
assert longest([""]) == ""
