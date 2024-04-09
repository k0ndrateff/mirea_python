from distance import distance


def distance_test():
    x1 = float(input("x1 -> "))
    y1 = float(input("y1 -> "))
    x2 = float(input("x2 -> "))
    y2 = float(input("y2 -> "))

    assert distance(x1, y1, x2, y2) == ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


distance_test()
