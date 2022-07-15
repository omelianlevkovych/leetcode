class Solution:
    def toLowerCase(self, s: str) -> str:
        print(self.toLower(s))
        return self.toLower(s)
    
    def toLower(self, s: str) -> str:
        symbols = list(s)
        
        for i in range(len(s)):
            symbols[i] = symbols[i].lower()
        
        
        return ''.join(symbols)