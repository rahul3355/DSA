def twoSum(array, targetSum):
    # O(n) time | O(n) space
    nums = {}
    for number in array:
        potentialMatch = targetSum - number
        if potentialMatch in nums:
            return [potentialMatch, number]
        nums[number] = True
    return []
