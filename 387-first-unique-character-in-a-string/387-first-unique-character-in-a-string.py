class Solution:
    def firstUniqChar(self, s: str) -> int:
        M = {}
        
        for i in range(0, len(s)):
            if s[i] in M:
                M[s[i]] += 1
            else:
                M[s[i]] = 1
        
        for i in range(0, len(s)):
            if M[s[i]] == 1:
                return i
        
        return -1