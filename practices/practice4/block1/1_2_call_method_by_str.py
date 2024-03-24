# Напишите код, который по имени метода, заданному строкой, вызовет этот метод
# в объекте некоторого пользовательского класса.


class Circle:
    def __init__(self, color: str, radius: float, stroke_width: float):
        self.color = color
        self.radius = radius
        self.stroke_width = stroke_width

    def get_length(self) -> float:
        return 2 * 3.14159 * self.radius

    def set_color(self, color: str) -> None:
        self.color = color


def call(obj: object, method: str):
    result = getattr(obj, method)
    return result()


def main():
    circle = Circle("red", 10, 2)
    length = call(circle, 'get_length')
    print(length)


if __name__ == '__main__':
    main()
