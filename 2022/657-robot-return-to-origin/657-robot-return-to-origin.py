class Solution:
    def judgeCircle(self, moves: str) -> bool:
        lr = 0
        ud = 0
        
        for m in moves:
            if m is 'L':
                lr -= 1
            if m is 'R':
                lr += 1
            if m is 'U':
                ud += 1
            if m is 'D':
                ud -= 1
        
        return ud == 0 and lr == 0