class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # use stack
        # when stack empty its a sub-string
        arr = list(s)
        stack = []
        stack.append(arr[0])
        
        res = 0
        
        for i in range(1, len(s)):
            
            if not stack:
                res += 1
                stack.append(arr[i])
                continue

            if stack[-1] == arr[i]:
                stack.append(arr[i])
            
            if stack[-1] != arr[i]:
                stack.pop()
            
        return res + 1
            
