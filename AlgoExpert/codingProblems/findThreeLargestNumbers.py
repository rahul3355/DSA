def findThreeLargestNumbers(array):
    # O(n) time | O(1) space
    firstLargest = -10000
    secondLargest = -10000
    thirdLargest = -10000

    for i in range(len(array)):
        if array[i] >= firstLargest:
            temp1 = firstLargest
            temp2 = secondLargest
            firstLargest = array[i]
            secondLargest = temp1
            thirdLargest = temp2
        elif array[i] < firstLargest and array[i] >= secondLargest:
            temp = secondLargest
            secondLargest = array[i]
            thirdLargest = temp
        elif array[i] < firstLargest and array[i] < secondLargest and array[i] >= thirdLargest:
            thirdLargest = array[i]
    return [thirdLargest, secondLargest, firstLargest]