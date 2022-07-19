class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        def summ(j, arr):
            summ_res = 0
            
            for i in range(0, len(arr)):
                if i == j:
                    continue
                if arr[i] == 1:
                    summ_res += abs(i - j)          
            return summ_res
        
        nums = list(map(int, boxes))
        ans = []
        for i in range(0, len(nums)):
            ans.append(summ(i, nums))
        
        return ans
        
        