def binarySearch(array, target):
    # O(log(n)) time | O(1) space
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        if target > array[middle]:
            left = middle + 1
        elif target < array[middle]:
            right = middle - 1
        else:
            return middle
    return -1
