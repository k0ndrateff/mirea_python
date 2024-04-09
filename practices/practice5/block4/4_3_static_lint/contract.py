import deal


@deal.ensure(lambda arr, x, result: result > 0 if x in arr else -1)
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
