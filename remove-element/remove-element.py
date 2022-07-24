class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k = n
        
        # nums = [3,2,2,3], val = 3
        # Output: 2, nums = [2,2,_,_]
        
        for i in range(n - 1, -1, -1):
            if nums[i] == val:
                k -= 1
                for j in range(i, n - 1):
                    nums[j] = nums[j + 1]
        
        print(nums)
        return k