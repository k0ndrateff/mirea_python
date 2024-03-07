# Вы получили зашифрованное сообщение и теперь предстоит его расшифровать.
# Известно, что для зашифрования использовался алгоритм TEA.
# Известен также ключ зашифрования/расшифрования.
# Имеется и функция на C/C++ для расшифровки данных.
# Остается перевести функцию decrypt на Питон и узнать,
# что же содержится в зашифрованном сообщении!

def convert_str_to_32_bit_int(v: str) -> int:
    result = 0
    for char in v:
        result = (result << 8) + ord(char)

    return result


def convert_32_bit_int_to_str(v: int) -> str:
    result = ""
    for _ in range(4):
        result = chr(v & 0xFF) + result
        v >>= 8

    return result


def decrypt(v: str, k: [int, int, int, int]) -> str:
    v0 = convert_str_to_32_bit_int(v[:4])
    v1 = convert_str_to_32_bit_int(v[4:])
    s = 0xC6EF3720
    delta = 0x9E3779B

    for i in range(32):
        v1 -= ((v0 << 4) + k[2]) ^ (v0 + s) ^ ((v0 >> 5) + k[3])
        v0 -= ((v1 << 4) + k[0]) ^ (v1 + s) ^ ((v1 >> 5) + k[1])
        s -= delta

    return f'{convert_32_bit_int_to_str(v0)}{convert_32_bit_int_to_str(v1)}'


def main():
    message = ('E32385576204A1F8E6537611174E57475D954DA88C2DFE972911CB4C2CB7C'
               '66BE7F185A0C7E3FA4042419867374044DF2519F07D5A0C24D4F4A960C531'
               '159418F2768EC7AEAF14CF071B2C95C9F22699FFB06F412AC90051A53F035'
               'D830601A7EB475702183BAA6F126267449B75A72F8DBFBFEC73C1A46EFFB0'
               '6F412AC9005197C5E4E9B1C26A21DD4A34636B71162F8C0756687975D5656'
               'D95A7007272E637')
    k = [0, 4, 5, 1]

    result = ''
    for i in range(0, len(message), 8):
        result += decrypt(message[i:i+8], k)

    print(result)


if __name__ == '__main__':
    main()
