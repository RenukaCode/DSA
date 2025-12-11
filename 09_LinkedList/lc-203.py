# lc - 203. Remove Linked List Elements
""""""
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
""""""    
class Solution:
    def removeElements(self, head, val):
        temp = Node(0)
        temp.next = head
        curr = temp
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return temp.next
"""
    def display(self, head):
        temp = head
        while temp:
            print(temp.val, end = "->")
            temp = temp.next
        print("None")
"""
# Example usage:
"""
head = Node(1)
head.next = Node(2)
head.next.next = Node(6)
head.next.next.next = Node(3)
head.next.next.next.next = Node(6)
sol = Solution() 
sol.display(head)                        # 1->2->6->3->6->None
head = sol.removeElements(head, 6)
sol.display(head)                        # 1->2->3->None
"""