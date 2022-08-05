class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        ans = [0] * 2*n
        
        i = 0
        j = n
        
        for k in range(0, 2 * n - 1, 2):
            ans[k] = nums[i]
            ans[k + 1] = nums[j]
            
            i += 1
            j += 1
        
        return ans