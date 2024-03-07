# Проверить, относится ли число к числам харшад
# (делящиеся нацело на сумму своих цифр).


def is_harshad(num: int) -> bool:
    return num % sum(map(int, str(num))) == 0


assert is_harshad(10)
assert is_harshad(1729)
assert not is_harshad(41)
