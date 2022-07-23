class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # [1,2,3,0,0,0], [2,5,6] -> [1,2,2,3,5,6]
        # two pointers?
        
        # [2, 0]
        # 1
        # [1]
        # 1
        # output: [2,2]
        
        i = m - 1    
        j = n - 1

        for q in range(m + n - 1, -1, -1):
            print(q, i, j)
            if i < 0:
                nums1[q] = nums2[j]
                j -= 1
                continue
                
            if j < 0:
                nums1[q] = nums1[i]
                i -= 1
                continue
                
            if nums1[i] > nums2[j]:
                nums1[q] = nums1[i]
                i -= 1
                
            else:
                nums1[q] = nums2[j]
                j -= 1