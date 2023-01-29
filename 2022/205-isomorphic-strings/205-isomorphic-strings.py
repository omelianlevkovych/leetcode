class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        M = {}
        
        for i in range(0, len(s)):
            if s[i] not in M:
                if t[i] in M.values():
                        return False
                M[s[i]] = t[i]
            elif M[s[i]] != t[i]:
                return False
        
        
        return True