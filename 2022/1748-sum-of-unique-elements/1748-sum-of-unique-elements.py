class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashmap = {}
        
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        res = 0;
        for i in hashmap:
            if hashmap[i] == 1:
                res += i
        return res