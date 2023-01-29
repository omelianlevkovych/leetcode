class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        def match(item, ruleKey, ruleValue):
            if ruleKey == "type":
                return item[0] == ruleValue
            if ruleKey == "color":
                return item[1] == ruleValue
            if ruleKey == "name":
                return item[2] == ruleValue
        
        
        res = 0
        
        for i in items:
            if match(i, ruleKey, ruleValue):
                res += 1
        
        return res