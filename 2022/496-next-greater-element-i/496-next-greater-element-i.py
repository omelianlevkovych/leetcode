class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        def find(x, array):
            for i in range(0, len(array)):
                if array[i] == x:
                    return i
        
        ans = []
        
        for el in nums1:
            index = find(el, nums2)
            a = -1
            for i in range(index, len(nums2)):
                if el < nums2[i]:
                    a = nums2[i]
                    break
            ans.append(a)
        return ans
            
        