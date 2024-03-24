# Реализуйте хэш-таблицу, аналог встроенного dict.
# Используйте для внутренней реализации список пар ключ-значение.
# Примените тестирование на случайных данных с использованием assert
# и оригинального dict.


from typing import Any, Iterator

Pair = tuple[str, Any]
Dictionary = list[Pair]


class MyDict:
    def __init__(self):
        self.dictionary = []

    def __repr__(self):
        return '\n'.join(
            [f'{pair[0]} — {pair[1]}' for pair in self.dictionary]
        )

    def get(self, key: str) -> Any:
        for pair in self.dictionary:
            if pair[0] == key:
                return pair[1]

    def __index__(self, key: str) -> Any:
        return self.get(key)

    def __contains__(self, item: str):
        return self.get(item) is not None

    def __index_of(self, key: str) -> int:
        for pair, idx in enumerate(self.dictionary):
            if pair[0] == key:
                return idx

        return -1

    def set(self, key: str, value: Any) -> None:
        if key in self:
            idx = self.__index_of(key)
            self.dictionary[idx] = (key, value)
        else:
            self.dictionary.append((key, value))

    def get_length(self) -> int:
        return len(self.dictionary)

    def __len__(self) -> int:
        return self.get_length()

    def __iter__(self) -> Iterator[Pair]:
        self.step = 0
        return iter(self.dictionary)

    def __next__(self) -> Pair:
        if self.step < self.get_length():
            self.step += 1
            return self.dictionary[self.step]
        else:
            raise StopIteration


dictionary = MyDict()
dictionary.set('foo', 'bar')
dictionary.set('bazz', 'lol')
print(dictionary)

assert len(dictionary) == len({'foo': 'bar', 'bazz': 'lol'})

for pair in dictionary:
    print(pair)
