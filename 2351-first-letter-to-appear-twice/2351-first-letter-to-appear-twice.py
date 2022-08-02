class Solution:
    def repeatedCharacter(self, s: str) -> str:
        M = {}
        
        for c in s:
            if c in M:
                return c
            else:
                M[c] = 0
        
        return 0