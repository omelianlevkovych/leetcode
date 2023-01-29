# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        
        fir,sec = headA, headB
        
        while fir != sec:
            if fir == None:
                fir = headB
            else:
                fir = fir.next
            
            if sec == None:
                sec = headA
            else:
                sec = sec.next
        
        return fir