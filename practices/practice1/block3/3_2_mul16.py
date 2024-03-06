# Умножение на 16. Используйте 4 сложения.

def mul16(x):
    result = x
    result += result  # 2x
    result += result  # 4x
    result += result  # 8x
    result += result  # 16x
    return result


print(mul16(5))
