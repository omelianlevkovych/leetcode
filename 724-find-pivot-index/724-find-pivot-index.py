class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumL = 0
        sumR = 0
        
        n = len(nums)
        
        for i in range(1, n):
            sumR += nums[i]
        
        for i in range(0, n - 1):
            print(sumL, sumR)
            if sumL == sumR:
                return i
            
            sumL += nums[i]
            sumR -= nums[i + 1]
        
        if sumL == 0:
            return n - 1
        
        return -1