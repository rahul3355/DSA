
class Solution:
    def firstBadVersion(self, n: int) -> int:
        min = 1
        max = n

        while min < max:
            
            mid = min + (max - min) // 2
            flag = isBadVersion(mid)
            
            if flag == False:
                min = mid + 1
            elif flag == True :
                max = mid
            
                
        return max