class Solution(object):
    def twoSum(self, nums, target):
        
        numsMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in numsMap:
                return [i, numsMap[diff]]
            numsMap[n] = i
        return