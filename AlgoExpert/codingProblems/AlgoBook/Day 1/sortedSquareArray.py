def sortedSquaredArray(array):
    # O(n) time | O(n) space
    newArr = [0 for _ in range(len(array))]
    smallerIdx = 0
    largerIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        largerValue = array[largerIdx]
        smallerValue = array[smallerIdx]
        if abs(smallerValue) > abs(largerValue):
            newArr[idx] = smallerValue * smallerValue
            smallerIdx += 1
        else:
            newArr[idx] = largerValue * largerValue
            largerIdx -= 1
    return newArr