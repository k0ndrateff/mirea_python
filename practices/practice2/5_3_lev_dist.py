from functools import cache


@cache
def f(a: str, b: str, i: int, j: int) -> int:
    if i == 0 or j == 0:
        return max(i, j)
    elif a[i - 1] == b[j - 1]:
        return f(a, b, i - 1, j - 1)
    else:
        return 1 + min(
            f(a, b, i, j - 1), f(a, b, i - 1, j), f(a, b, i - 1, j - 1)
        )


def lev_dist(s1: str, s2: str) -> int:
    return f(s1, s2, len(s1), len(s2))


print(lev_dist('столб', 'слон'))