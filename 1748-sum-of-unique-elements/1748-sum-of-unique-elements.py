class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        n = len(nums)
        s = sorted(nums)
        
        if n == 1:
            return nums[0]
        
        ans = 0
        if s[0] != s[1]:
            ans += s[0]
        if s[n - 1] != s[n - 2]:
            ans += s[n - 1]
        
        print(s)
        
        for i in range(1, n - 1):
            if s[i] != s[i - 1] and s[i] != s[i + 1]:
                ans += s[i]        
        
        return ans