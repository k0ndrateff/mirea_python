# Реализовать рекурсивную функцию

def main(n):
    if n == 0:
        return -0.76
    else:
        return (43 * main(n - 1) ** 2 - 92 * main(n - 1)) / 91
