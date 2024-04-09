import pytest

from triangle import distance, triangle_type


@pytest.fixture
def points():
    return 0, 0, 1, 1, 2, 2


@pytest.fixture
def equilateral_points():
    return 0, 0, 1, 1, 0, 1


@pytest.mark.parametrize("points, expected_type", [
    ((0, 0, 1, 1, 2, 2), "равнобедренный"),
    ((0, 0, 1, 1, 0, 1), "равнобедренный"),
    ((0, 0, 1, 2, 3, 4), "разносторонний")
])
def test_triangle_type(points, expected_type):
    x1, y1, x2, y2, x3, y3 = points
    assert triangle_type(x1, y1, x2, y2, x3, y3) == expected_type
