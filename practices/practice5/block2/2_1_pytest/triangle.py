def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def triangle_type(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    if a == b == c:
        return "равносторонний"
    elif a == b or a == c or b == c:
        return "равнобедренный"
    elif a != b != c:
        return "разносторонний"

