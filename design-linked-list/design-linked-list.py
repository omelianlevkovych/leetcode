class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.head
        
        for i in range(0, index):
            cur = cur.next
        
        return cur.val

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        cur = self.head
        newNode = Node(val)
        
        if index <= 0:
            newNode.next = cur
            self.head = newNode
        
        else:
            for i in range(0, index - 1):
                cur = cur.next
            newNode.next = cur.next
            cur.next = newNode
        
        self.size += 1
    
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        cur = self.head
        
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(0, index - 1):
                cur = cur.next
            cur.next = cur.next.next
        
        self.size -= 1