# Time Complexity: O(n)
# Space Complexity: O(1)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def deleteAllOccurences(self, head):
        temp = head
        while temp and temp.next:
            if temp.next.value == head.value:
                temp.next = temp.next.next
            temp = temp.next
        return head
"""
    def display(self, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")
head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(3)
head.next.next.next.next = Node(1)
ll = LL()
ll.display(head)                     #1->2->1->3->1->None
new_head = ll.deleteAllOccurences(head)
ll.display(new_head)                 #1->2->3->None"""

