class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # [2,2,3,1]
        
        m1 = m2 = m3 = -float("inf")
        
        for n in nums:
            if n > m1:
                m1,m2,m3 = n, m1, m2
            elif m2 < n < m1:
                m2,m3 = n, m2
            elif m3 < n < m2:
                m3 = n
            
        if m3 > -float("inf"):
            return m3
        return m1
        