class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_row = 0
        res = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                count_row = 0
            else:
                count_row += 1
                res = max(res, count_row)
        
        
        return res