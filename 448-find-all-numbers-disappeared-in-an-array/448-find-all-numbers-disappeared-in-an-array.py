class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(0,n):
            t = abs(nums[i]) - 1
            if nums[t] > 0:
                nums[t] *= -1
                
        # now find the positive numbers, such numbers that there no such number that number + 1 will be it index
        ans = []
        for i in range(0, n):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans