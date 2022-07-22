class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def isEven(num):
            digits = 0
            
            while num > 0:
                digits += 1
                num = num // 10
            return digits % 2 == 0
        
        ans = 0
        
        for i in nums:
            if isEven(i):
                ans += 1
        
        return ans
        