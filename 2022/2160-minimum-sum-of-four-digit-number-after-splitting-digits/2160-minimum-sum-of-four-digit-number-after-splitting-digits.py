class Solution:
    def minimumSum(self, num: int) -> int:
        n = list(map(int, str(num)))
        
        n = sorted(n)
        return (n[0] + n[1])*10 + n[2] + n[3]