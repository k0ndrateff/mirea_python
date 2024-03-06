# Умножение на 15. Используйте 3 сложения и 2 вычитания.

def mul15(x):
    result = x
    result += result  # 2x
    result += result  # 4x
    result += result  # 8x
    result += result  # 16x

    return result - x


print(mul15(1))
