# https://github.com/rahul3355/DSA.git

class Solution(object):
    def containsDuplicate(self, nums):
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        return False