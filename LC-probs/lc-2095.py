# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def __init__(self):
        self.head = None
    def delMidEle(self):
        if not self.head or not self.head.next:
            self.head = None
            return
        fast = slow = self.head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
"""    
    def display(self):
        temp = self.head
        while temp:
            print(temp.value, end = "<->")
            temp = temp.next
        print("None")"""
"""
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
ll = LL()
ll.head = head
ll.display()                        #10<->20<->30<->40<->50<->None
ll.delMidEle()                      
ll.display()                        #10<->20<->40<->50<->None"""



        

