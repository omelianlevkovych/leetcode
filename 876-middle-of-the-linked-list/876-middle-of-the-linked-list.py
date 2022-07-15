# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head

        def getSize(head):
            if head is None:
                return 0
            return 1 + getSize(head.next)
        
        n = getSize(head)
        n = n // 2
        
        for i in range(0, n):
            pointer = pointer.next
        print(pointer.val)
        return pointer