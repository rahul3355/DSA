class Solution(object):
    def containsDuplicate(self, nums):
        mapNums = {}
        for num in nums:
            if num not in mapNums:
                mapNums[num] = True
            else:
                return True
        return False