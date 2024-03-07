# Сгенерировать случайную текстовую строку с заданным максимальным размером.


import random
import string


def generate_random_string(length: int) -> str:
    return ''.join(random.choice(string.ascii_letters) for i in range(length))


print(generate_random_string(10))
print(generate_random_string(10))
print(generate_random_string(100))