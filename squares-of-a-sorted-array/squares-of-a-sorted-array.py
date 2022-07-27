class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        ans = [0] * n
        
        # p - pointer, start writing from the end
        write_p = n - 1
        left_p = 0
        right_p = n - 1
        
        while write_p >= 0:
            if abs(arr[left_p]) > abs(arr[right_p]):
                ans[write_p] = arr[left_p] ** 2
                left_p += 1
            else:
                ans[write_p] = arr[right_p] ** 2
                right_p -= 1
            
            write_p -= 1
            
        return ans