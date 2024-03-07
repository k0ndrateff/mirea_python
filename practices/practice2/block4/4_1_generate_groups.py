# Напишите функцию generate_groups(), которая компактно генерирует
# (а не просто выдает готовый) список всех названий групп в том виде,
# который используется на сайте ЦАП.
# Результат оценивается с точки зрения размера кода и его читаемости.


def generate_groups() -> list[str]:
    courses = [('B', 9, []), ('К', 37, [10, 24, 29, 34]),
               ('М', 2, []), ('Н', 12, [])]
    # Каждый курс состоит из буквы направления, количества групп, и списка
    # номеров групп, которые нужно исключить из списка

    result = []

    for course in courses:
        for group_number in range(1, course[1] + 1):
            if group_number in course[2]:
                continue
            result.append(f'И{course[0]}БО-{group_number:02d}-22')

    return result


print(generate_groups())
