class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxN = 0
        
        for s in sentences:
            sent_l = 0
            print(s)
            for w in s.split(" "):
                sent_l += 1
            
            if maxN < sent_l:
                maxN = sent_l
        
        return maxN