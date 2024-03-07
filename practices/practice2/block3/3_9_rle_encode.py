# Реализовать функцию-однострочник для RLE-сжатия.


from itertools import groupby


def rle_encode(s: str) -> list[(str, int)]:
    return [x for x in ((x, sum(1 for _ in y)) for x, y in groupby(s))]


assert rle_encode("AABB") == [('A', 2), ('B', 2)]
assert rle_encode("ABBCCCDEF") == [('A', 1), ('B', 2), ('C', 3), ('D', 1), ('E', 1), ('F', 1)]
