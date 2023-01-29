class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        
        def countOf1(b):
            ans = 0
            for i in b:
                if i == '1':
                    ans += 1
            return ans
        
        amount = []
        for r in bank:
            a = countOf1(r)
            if a > 0:
                amount.append(countOf1(r))
        
        res = 0
        
        print(amount)
        
        for i in range(0, len(amount) - 1):
            if amount[i] == 0:
                continue
            if amount[i] != 1 and amount[i + 1] == 1:
                res += amount[i]
            else:
                res += amount[i] * amount[i + 1]
        
        return res