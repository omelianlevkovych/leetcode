class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                t = nums[j]
                nums[j] = nums[i]
                nums[i] = t
                j += 1
        print(nums)