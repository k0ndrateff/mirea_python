# Напишите код, который выведет на экране все имена полей объекта произвольного
# пользовательского класса, кроме служебных имен.


class Circle:
    def __init__(self, color: str, radius: float, stroke_width: float):
        self.color = color
        self.radius = radius
        self.stroke_width = stroke_width


def main():
    circle = Circle('red', 10, 2)

    for field in circle.__dict__.keys():
        print(field)


if __name__ == '__main__':
    main()
