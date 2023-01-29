class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # if same i + = 1
        
        n = len(nums)
        
        i = 0

        for i in range(0, n):
            if nums[i] == nums[nums[i] - 1]:
                continue
            while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                t = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = t

            
        ans = []
        for i in range(0, n):
            if nums[i] != i + 1:
                ans.append(i + 1)
                
        return ans