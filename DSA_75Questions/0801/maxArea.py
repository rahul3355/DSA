class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i=0
        j=len(height)-1
        while j>i:
            area = abs(j-i)*min(height[i], height[j])
            if area>max_area:
                max_area = area
            if height[i]>height[j]:
                j = j-1
            else:
                i = i+1
        return max_area