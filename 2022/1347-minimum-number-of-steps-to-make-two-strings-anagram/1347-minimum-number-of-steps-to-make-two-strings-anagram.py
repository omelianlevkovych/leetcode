class Solution:
    def minSteps(self, s: str, t: str) -> int:
        D = {}
        for c in s:
            if c in D:
                D[c] += 1
            else:
                D[c] = 1
        res = 0
        
        for c in t:
            if c in D and D[c] != 0:
                D[c] -= 1
            else:
                res += 1
        
        return res