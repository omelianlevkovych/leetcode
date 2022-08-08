class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def selfdivided(x):
            digits = map(int, str(x))
            
            for d in digits:
                if d == 0 or x % d != 0:
                    return False
            return True
        
        ans = []
        
        for i in range(left, right + 1):
            if selfdivided(i):
                ans.append(i)
                
        
        return ans