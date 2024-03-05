import random

text_starts = ['Коллеги,']
sentence_starts = ['В то же время,', 'Однако,', 'Тем не менее,',
                   'Следовательно,', 'Соответственно,', 'Вместе с тем,',
                   'С другой стороны,']
level_2 = ['парадигма цифровой экономики', 'контекст цифровой трансформации',
           'диджитализация бизнес-процессов',
           'прагматичный подход к цифровым платформам',
           'совокупность сквозных технологий',
           'программа прорывных исследований', 'ускорение блокчейн-транзакций',
           'экспоненциальный рост Big Data']
level_3 = ['открывает новые возможности для', 'выдвигает новые требования',
           'несёт в себе риски', 'расширяет горизонты',
           'заставляет искать варианты', 'не оставляет шанса для',
           'повышает вероятность', 'обостряет проблему']
level_4 = ['дальнейшего углубления', 'бюджетного финансирования',
           'синергетического эффекта', 'компрометации конфиденциальных',
           'универсальной коммодитизации', 'несанкционированной кастомизации',
           'нормативного регулирования', 'практического применения']
level_5 = ['знаний и компетенций.', 'непроверенных гипотез.',
           'волатильных активов.', 'опасных экспериментов.',
           'государственно-частных партнёрств.', 'цифровых следов граждан.',
           'нежелательных последствий.', 'внезапных открытий.']


def choose_phrase(phrases: list[str]) -> str:
    return random.choice(phrases)


def generate_sentence(start: list[str]) -> str:
    return (f'{choose_phrase(start)} {choose_phrase(level_2)} '
            f'{choose_phrase(level_3)} {choose_phrase(level_4)} '
            f'{ choose_phrase(level_5)}')


def generate_normal_sentence() -> str:
    return generate_sentence(sentence_starts)


def generate_first_sentence() -> str:
    return generate_sentence(text_starts)


def generate_paragraph(number_of_sentences: int, is_first: bool) -> str:
    if is_first:
        paragraph = generate_first_sentence() + ' '
    else:
        paragraph = generate_normal_sentence() + ' '

    for i in range(number_of_sentences - 1):
        paragraph += generate_normal_sentence() + ' '

    return paragraph


def generate_text() -> str:
    text = generate_paragraph(3, True) + '\n\n'

    for i in range(3):
        text += generate_paragraph(3, False) + '\n\n'

    return text


def main():
    print(generate_text())


if __name__ == '__main__':
    main()
