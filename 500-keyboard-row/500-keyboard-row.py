class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = { "q", "w", "e", "r", "t", "y", "u", "i", "o", "p" }
        set2 = { "a", "s", "d", "f", "g", "h", "j", "k", "l" }
        set3 = { "z", "x", "c", "v", "b", "n", "m"}
        
        def checkFunc(w, setx):
            for c in w:
                if c not in setx:
                    return False
            return True
        
        def success(word):
            if len(word) < 2:
                return True
            
            word = word.lower()
            
            if word[0] in set1:
                return checkFunc(word, set1)
            
            elif word[0] in set2:
                return checkFunc(word, set2)
            elif word[0] in set3:
                return checkFunc(word, set3)
            else:
                return False
        
        ans = []
        
        for w in words:
            if success(w):
                ans.append(w)
        
        return ans