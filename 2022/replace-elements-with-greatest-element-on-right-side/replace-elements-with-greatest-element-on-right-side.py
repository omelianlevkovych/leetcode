class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return [-1]
        
        n = len(arr)
        
        maxv = arr[n - 1]
        
        for i in range(n - 1, 0, -1):
            if arr[i] > maxv:
                maxv = arr[i]              
            t = arr[i - 1]
            arr[i - 1] = maxv
            if t > maxv:
                maxv = t
        
        arr[n - 1] = -1
        
        return arr