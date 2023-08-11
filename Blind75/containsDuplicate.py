class Solution(object):
    def containsDuplicate(self, nums):
        hashSet = set()

        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        
        return False

        # O(n) time | O(n) space