class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if not arr:
            return False
        
        n = len(arr)
        
        if n < 3:
            return False
        
        j = 0
        for i in range(0, n-1):
            if arr[i + 1] <= arr[i]:
                j = i
                break
        
        if j == 0:
            return False
        
        for i in range(j, n-1):
            if arr[i + 1] >= arr[i]:
                print(i)
                return False
        
        return True