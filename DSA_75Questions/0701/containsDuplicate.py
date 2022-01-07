class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        
        for num in nums:
            if num not in hashSet:
                hashSet.add(num)
            else:
                return True
        return False