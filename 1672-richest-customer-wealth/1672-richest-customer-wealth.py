class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0;
        for i in range (0, len(accounts)):
            val = 0;
            for j in range(0, len(accounts[i])):
                val += accounts[i][j];
            if val > maximum :
                maximum = val;
        
        return maximum;