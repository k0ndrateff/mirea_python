from functools import cache


@cache
def f(a: str, b: str, i: int, j: int) -> int:
    if i == 0 or j == 0:
        return max(i, j)
    elif a[i - 1] == b[j - 1]:
        return f(a, b, i - 1, j - 1)
    else:
        insert = f(a, b, i, j - 1)
        delete = f(a, b, i - 1, j)
        replace = f(a, b, i - 1, j - 1)
        mi = min(insert, delete, replace)

        if insert == mi:
            print('ins')
        elif delete == mi:
            print('del')
        elif replace == mi:
            print('rep')

        return 1 + mi


def lev_dist(s1: str, s2: str) -> int:
    return f(s1, s2, len(s1), len(s2))


print(lev_dist('столб', 'слон'))