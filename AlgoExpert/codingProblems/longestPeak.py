def longestPeak(array):
    # Write your code here.

    if len(array) == 0:
        return 0

    
    biggestTip, tipIndex = findBiggestTip(array)

    print("Biggest Tip: ", biggestTip)
    print("Tip Index: ", tipIndex)

    if biggestTip == 0 or tipIndex == 0:
        return 0

    leftElements = findNumberOfLeftElements(array, biggestTip, tipIndex)
    rightElements = findNumberOfRightElements(array, biggestTip, tipIndex)

    lengthOfLongestPeak = leftElements + rightElements + 1
    
    return lengthOfLongestPeak


def findNumberOfLeftElements(array, biggestTip, tipIndex):
    count = 0
    for i in range(tipIndex, -1, -1):
        if(array[i] <= array[i-1]):
            return count
        else:
            count += 1

    return count


def findNumberOfRightElements(array, biggestTip, tipIndex):
    count = 0
    for i in range(tipIndex, len(array)-1):
        if(array[i] <= array[i+1]):
            return count
        else:
            count += 1

    return count
    


def findBiggestTip(array):
    currentBiggestTip, currentIndex = 0, 0
    for i in range(1, len(array)-1):
        x = array[i]
        if array[i-1] < x and array[i + 1] < x and x > currentBiggestTip:
            currentBiggestTip = x
            currentIndex = i

    return currentBiggestTip, currentIndex
