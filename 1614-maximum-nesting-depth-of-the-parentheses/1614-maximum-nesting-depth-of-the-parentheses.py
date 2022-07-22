class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        ans = 0
        
        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(s[i])
            if stack and s[i] == ')' and stack[-1] == '(':
                stack.pop()
                ans = max(len(stack) + 1, ans)
        
        return ans