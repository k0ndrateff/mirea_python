# Умножение на 12. Используйте 4 сложения.

def mul12(x):
    result2 = x
    result2 += result2  # 2x
    result2 += result2  # 4x
    result = result2
    result += result  # 8x
    result += result2  # 8x + 4x = 12x
    return result


print(mul12(5))
