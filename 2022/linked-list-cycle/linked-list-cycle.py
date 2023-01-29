# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            print(1)
            return False
        if head.next == None or head.next.next == None:
            print(2)
            return False
        
        one = head
        two = head.next.next
        
        while two != one:
            print(3)
            if two.next == None or two.next.next == None:
                return False
            
            two = two.next.next
            one = one.next
        
        return True