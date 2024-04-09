import random


def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr


def test_bucketsort_random():
    arr = [random.randint(0, 9) for _ in range(10)]
    k = 10
    sorted_arr = bucketsort(arr, k)
    assert sorted_arr == sorted(arr), "Incorrect sorting of random data"


def test_bucketsort_specification():
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    k = 10
    sorted_arr = bucketsort(arr, k)

    for num in arr:
        assert sorted_arr.count(num) == arr.count(
            num), f"Element {num} count mismatch"

    assert all(sorted_arr[i] <= sorted_arr[i + 1] for i in
               range(len(sorted_arr) - 1)), "Array is not sorted"


if __name__ == '__main__':
    test_bucketsort_random()
    test_bucketsort_specification()