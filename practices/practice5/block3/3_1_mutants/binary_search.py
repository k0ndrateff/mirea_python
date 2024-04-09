def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def test_binary_search():
    # Тест на нахождение элемента в списке
    arr = [1, 3, 5, 7, 9, 11]
    x = 5
    assert binary_search(arr, x) == 2

    # Тест на отсутствие элемента в списке
    arr = [1, 3, 5, 7, 9, 11]
    x = 6
    assert binary_search(arr, x) == -1

    # Тест на нахождение первого элемента
    arr = [1, 3, 5, 7, 9, 11]
    x = 1
    assert binary_search(arr, x) == 0

    # Тест на нахождение последнего элемента
    arr = [1, 3, 5, 7, 9, 11]
    x = 11
    assert binary_search(arr, x) == 5

    # Тест на пустой список
    arr = []
    x = 5
    assert binary_search(arr, x) == -1

    # Тест на список с одним элементом
    arr = [5]
    x = 5
    assert binary_search(arr, x) == 0

    # Тест на список с повторяющимися элементами
    arr = [2, 2, 2, 2, 2]
    x = 2
    assert binary_search(arr, x) == 2

