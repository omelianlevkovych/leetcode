class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        j = 0
        
        for i in range(0, len(nums)):
            if nums[i] % 2 == 0:
                t = nums[j]
                nums[j] = nums[i]
                nums[i] = t
                j += 1
        
        return nums