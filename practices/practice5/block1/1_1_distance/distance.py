# Исправьте функцию distance. Добавьте документацию к функции
# в виде docstring-строки. Укажите примеры в формате doctest.
# Примеры должны охватывать граничные случаи. Протестируйте программу
# с помощью вызова модуля doctest. Перенесите примеры в отдельный файл
# и снова протестируйте программу.


def distance(x1, y1, x2, y2):
    """
    Calculate the distance between two points in a 2D plane.

    Parameters:
    x1 (int): x-coordinate of the first point
    y1 (int): y-coordinate of the first point
    x2 (int): x-coordinate of the second point
    y2 (int): y-coordinate of the second point

    Returns:
    float: The distance between the two points
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5



