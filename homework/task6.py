from math import ceil


def main(Delta):
    P = {3 * delta for delta in Delta if delta > -93}
    Gamma = {delta ** 3 - abs(delta) for delta in Delta
             if delta < 67 or delta > 6}
    M = {p ** 3 + ceil(p / 4) for p in P if p >= -18}

    return len(Gamma) * len(M) + sum(M)

print(main({98, -62, -27, 42, 49, 20, -11, 28, 29, -97}))