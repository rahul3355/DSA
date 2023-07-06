def zeroSumSubarray(nums):
    # Write your code here.
    sumArray = []
    currSum = 0

    if len(nums) == 0:
        return False

    if nums[0] == 0:
        return True
    
    for i in range(len(nums)):
        currSum = nums[i] + currSum
        if currSum not in sumArray and currSum != 0:
            sumArray.append(currSum)
        else:
            return True
    return False
