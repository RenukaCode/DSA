# Time Complexity: O(n)
# Space Complexity: O(1)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def removeDups(self, head):
        if not head:
            return head
        curr = head
        while curr and curr.next:
            if curr.value == curr.next.value:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
    def display(self, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")
"""
head = Node(1)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(3)
ll = LL()
ll.display(head)                     #1->1->2->3->3->None
new_head = ll.removeDups(head)
ll.display(new_head)                 #1->2->3->None
"""