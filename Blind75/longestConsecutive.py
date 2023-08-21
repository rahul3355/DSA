class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for n in nums:
            #check for sequence start
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest

        # O(n) time | O(n) space