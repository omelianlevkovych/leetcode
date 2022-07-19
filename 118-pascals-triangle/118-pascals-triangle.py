class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
    
    #   1 [x1]
    #  1 1 [x1, x2]
    # 1 2 1 [x1, x2, x3]
    # recursion?
    
    # [x0 = 0, xn = 0]
    # x2 = x1 + x2, x3 = x2 + x3
    
        def next_level(prev):
            new = [1] * (len(prev) + 1)
            n = len(new)
            
            for i in range(1, n - 1):
                new[i] = prev[i - 1] + prev[i]
            return new
        
        ans = [[1]]
        cur = [1]
        for i in range(1, numRows):
            newRow = next_level(cur)
            ans.append(newRow)
            cur = newRow
        return ans