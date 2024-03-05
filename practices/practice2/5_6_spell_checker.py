from functools import cache
from unittest import result


@cache
def f(a: str, b: str, i: int, j: int) -> int:
    if i == 0 or j == 0:
        return max(i, j)
    elif a[i - 1] == b[j - 1]:
        return f(a, b, i - 1, j - 1)
    else:
        return 1 + min(f(a, b, i, j - 1),
                       f(a, b, i - 1, j),
                       f(a, b, i - 1, j - 1))


def lev_dist(s1: str, s2: str) -> int:
    return f(s1, s2, len(s1), len(s2))


def load_words(filename: str) -> dict[str, int]:
    d = {}
    with open(filename) as file:
        for line in file:
            (key, val) = line.split()
            d[str(key)] = int(val)

    return d


def process_token(token: str, words: dict[str, int]) -> str:
    token = token.lower()

    if token in words:
        return token
    else:
        for word in words:
            if lev_dist(token, word) == 1:
                return word

        for word in words:
            if lev_dist(token, word) == 2:
                return word

    return token


def main():
    res = ''
    dictionary = load_words("words.txt")
    message = input("Введите сообщение на русском: ")
    tokens = message.split(' ')

    for token in tokens:
        res += process_token(token, dictionary) + ' '

    print(res)


if __name__ == '__main__':
    main()
