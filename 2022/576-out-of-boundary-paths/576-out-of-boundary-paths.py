class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, i: int, j: int) -> int:
        
        # lookup how this is called
        dp = [[[-1]*(maxMove + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        
        
        def find(i, j, move):
            if move < 0:
                return 0
            
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
                    
            # if the dp array at this position contains some value(not -1) then it means it has been computed earlier
			# so we don't need to compute again, so return whatever value is present in dp.
            if dp[i][j][move] != -1:
                return dp[i][j][move]
            
            res = (find(i - 1, j, move - 1)
                   + find(i + 1, j, move - 1)
                   + find(i, j - 1, move - 1)
                   + find(i, j + 1, move - 1))
        
            dp[i][j][move] = res
            return res
        
        return find(i, j, maxMove) % 1000000007
        