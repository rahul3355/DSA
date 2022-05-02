class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = 0
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i] > target:
                    idx = i
                    break
                elif nums[len(nums)-1] < target:
                    idx = len(nums)
                    break
        return idx