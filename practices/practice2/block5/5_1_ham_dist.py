def ham_dist(num1: int, num2: int) -> int:
    dist = 0

    num1 = bin(num1)
    num2 = bin(num2)

    if len(num1) > len(num2):
        num2 = format(int(num2, 2), f'#0{len(num1)}b')
    elif len(num1) < len(num2):
        num1 = format(int(num1, 2), f'#0{len(num2)}b')

    for i in range(len(num1) - 1, -1, -1):
        if num1[i] != num2[i]:
            dist += 1

    return dist


print(ham_dist(0b1100, 0b0011))
