message = [815608, 2064837, 2093080, 2063879, 196608, 2067983, 10457031,
           1830912, 2067455, 2093116, 1044928, 2064407, 6262776, 2027968,
           4423680, 2068231, 2068474, 1999352, 1019903, 2093113, 2068439,
           2064455, 1831360, 1936903, 2067967, 2068456]


def most_frequent(n1: str, n2: str, n3: str) -> str:
    s = int(n1) + int(n2) + int(n3)
    if s > 1:
        return '1'
    else:
        return '0'


def decode_val(val: int) -> int:
    decoded = ''

    val = format(val, f'#026b')
    val = val[2:]

    for i in range(8):
        sl = val[i*3: i*3+3]
        decoded += most_frequent(sl[0], sl[1], sl[2])

    return int(decoded, 2)


def main():
    decoded_message = ''

    for c in message:
        decoded_message += chr(decode_val(c))

    print(decoded_message)


if __name__ == '__main__':
    main()