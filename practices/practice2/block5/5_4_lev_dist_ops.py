# Реализованная функция вычисления расстояния Левенштейна дает только
# минимальное число операций. Было бы полезно узнать, какие именно
# операции произведены над исходной строкой.
# Реализуйте функцию lev_dist_ops.


from functools import cache


@cache
def f(a: str, b: str, i: int, j: int) -> tuple:
    if i == 0 or j == 0:
        if i == 0 and j == 0:
            return ()
        elif i == 0:
            return ('добавление',) * j
        else:
            return ('удаление',) * i
    elif a[i - 1] == b[j - 1]:
        return f(a, b, i - 1, j - 1)
    else:
        del_op = f(a, b, i - 1, j) + ('удаление',)
        ins_op = f(a, b, i, j - 1) + ('добавление',)
        sub_op = f(a, b, i - 1, j - 1) + ('замена',)

        min_op = min(del_op, ins_op, sub_op, key=len)

        return min_op


def lev_dist_ops(s1: str, s2: str) -> list:
    return list(f(s1, s2, len(s1), len(s2)))


print(lev_dist_ops('столб', 'слон'))
