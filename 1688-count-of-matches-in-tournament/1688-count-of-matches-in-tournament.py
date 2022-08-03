class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return n // 2 + self.numberOfMatches(n // 2)
        else:
            x = (n - 1) // 2 + 1
            return (n - 1) // 2 + self.numberOfMatches(x)