class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        M = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
        
        for c in sentence:
            if c in M:
                M.remove(c)
        
        return len(M) == 0