def sortedSquaredArray(array):

    sortedSquareArray = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):

        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquareArray[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquareArray[idx] = largerValue * largerValue
            largerValueIdx -= 1

    return sortedSquareArray