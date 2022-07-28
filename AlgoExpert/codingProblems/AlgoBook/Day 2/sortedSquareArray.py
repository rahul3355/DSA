def sortedSquareArray(array):
    # O(n) time | O(n) space
    smallerIdx = 0
    largerIdx = len(array) - 1
    sortedSquareArray = [0 for _ in range(len(array))]

    for idx in reversed(range(len(array))):
        largerValue = array[largerIdx]
        smallerValue = array[smallerIdx]

        if abs(largerValue) > abs(smallerValue):
            sortedSquareArray[idx] = largerValue * largerValue
            largerIdx -= 1
        else:
            sortedSquareArray[idx] = smallerValue * smallerValue
            smallerIdx -= 1
        
    return sortedSquareArray

