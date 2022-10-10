def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    resultArr = []
    resultArrMain = []

    for i in range(len(array)-2):
        currNum = array[i]
        left = i+1
        right = len(array) - 1
        reqSum = targetSum - currNum

        while left < right:
            currSum = array[left] + array[right]
            if currSum == reqSum:
                resultArr.append([currNum, array[left], array[right]])
                left += 1
                right -= 1
            elif currSum > reqSum:
                right -= 1
            elif currSum < reqSum:
                left += 1

    return resultArr
            