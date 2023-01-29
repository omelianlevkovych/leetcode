class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # Input: nums = [3,2,2,3], val = 3
        # Output: 2, nums = [2,2,_,_]
        
        n = len(nums)
        
        j = 0
        for i in range(0, n):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        
        return j