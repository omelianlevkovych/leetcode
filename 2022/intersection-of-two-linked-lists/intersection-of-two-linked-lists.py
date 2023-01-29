# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        
        a,b = headA,headB
        
        while a != b:
            if a is None:
                a = headB
            else:
                a = a.next
            
            if b is None:
                b = headA
            else:
                b = b.next
        
        return a