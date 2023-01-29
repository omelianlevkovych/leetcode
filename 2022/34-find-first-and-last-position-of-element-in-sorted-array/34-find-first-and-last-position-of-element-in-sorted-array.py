class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        ans = [-1, -1]
        
        if not nums:
            return ans
        
        n = len(nums)
        
        low = 0
        up = n - 1
        
        while low <= up:
            midpoint = (low + up)//2
            
            if nums[midpoint] == target:
                ans[0], ans[1] = midpoint, midpoint
                break
                
            elif nums[midpoint] < target:
                low = midpoint + 1
            else:
                up = midpoint - 1
        
        if ans[0] == -1:
            return ans
        
        print(ans)
        
        while (ans[0] - 1) >= 0 and nums[ans[0] - 1] == target:
            ans[0] -= 1
            
        while (ans[1] + 1) < n and nums[ans[1] + 1] == target:
            ans[1] += 1
        
        return ans