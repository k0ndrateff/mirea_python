# Реализуйте простую языковую модель. Обучение модели производится
# на входном тексте с указанием длины префикса – глубины «памяти» модели.
# Для каждого префикса, извлеченного из текста, определяется
# частота встречаемости следуемого за префиксом символа. Более строго говоря,
# языковая модель основана на применении марковских цепей заданного порядка.


import random
from collections import defaultdict


def read_file(file_name: str) -> str:
    with open(file_name, "r") as f:
        text = f.read()
    return text


def train_model(text: str, prefix_length: int) -> dict[str, dict[str, int]]:
    model = defaultdict(dict)

    for i in range(len(text) - prefix_length):
        prefix = text[i:i + prefix_length]
        next_symbol = text[i + prefix_length]

        if next_symbol in model[prefix]:
            model[prefix][next_symbol] += 1
        else:
            model[prefix][next_symbol] = 1

    return model


def generate(model: dict[str, dict[str, int]], max_length: int) -> str:
    text = random.choice(list(model.keys()))
    current_prefix = text

    while len(text) < max_length:
        if current_prefix not in model:
            break

        next_symbols = model[current_prefix]
        total_frequency = sum(next_symbols.values())

        rand_num = random.randint(1, total_frequency)
        cumulative_frequency = 0

        for symbol, frequency in next_symbols.items():
            cumulative_frequency += frequency
            if rand_num <= cumulative_frequency:
                text += symbol
                current_prefix = current_prefix[1:] + symbol
                break

    return text


def main():
    train_data = read_file("pushkin.txt")
    model = train_model(train_data, 10)
    print(generate(model, 700))


if __name__ == "__main__":
    main()
