# Time Complexity: O(n)
# Space Complexity: O(1)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LL:
    def reverseLL(self, head):
        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev
    def addOne(self, head):
        head = self.reverseLL(head)
        curr = head
        carry = 1
        while curr and carry:
            sum_ = curr.value + carry
            curr.value = sum_ % 10
            carry = sum_ // 10
            if not curr.next and carry:
                curr.next = Node(carry)
                carry = 0
            curr = curr.next
        head = self.reverseLL(head)
        return head
    """
    def display(self, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")"""
"""
head = Node(9)
head.next = Node(9)
head.next.next = Node(9)
ll = LL()
ll.display(head)                         #9->9->9->None
new_head = ll.addOne(head)
ll.display(new_head)                     #1->0->0->0->None"""



# Recursive Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def addOne(self, head):
        if not head:
            return 1
        carry = self.addOne(head.next)
        total = head.value + carry
        head.value = total % 10
        return total // 10
    def addOneToList(self, head):
        carry = self.addOne(head)
        if carry:
            newHead = Node(carry)
            newHead.next = head
            head = newHead
        return head
    """
    def display(self, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")"""
"""
head = Node(9)
head.next = Node(9)
head.next.next = Node(9)
ll = LL()
ll.display(head)                         #9->9->9->None
new_head = ll.addOneToList(head)
ll.display(new_head)                     #1->0->0->0->None"""
