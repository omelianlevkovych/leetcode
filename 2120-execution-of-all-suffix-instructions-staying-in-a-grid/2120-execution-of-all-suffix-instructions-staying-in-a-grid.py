class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        
        def rec(n, x, y, moves, i):
            
            if i == len(moves):
                return 0
            
            if moves[i] == "R":
                if y == n - 1:
                    return 0
                return 1 + rec(n, x, y + 1, moves, i + 1)
            
            if moves[i] == "L":
                if y == 0:
                    return 0
                return 1 + rec(n, x, y - 1, moves, i + 1)
            
            if moves[i] == "U":
                if x == 0:
                    return 0
                return 1 + rec(n, x - 1, y, moves, i + 1)
            
            if moves[i] == "D":
                if x == n - 1:
                    return 0
                return 1 + rec(n, x + 1, y, moves, i + 1)
            
            
        moves = list(s)
 
        ans = []
        for i in range(0,len(moves)):
            a = rec(n, startPos[0], startPos[1], moves, i)
            ans.append(a)
            
        return ans