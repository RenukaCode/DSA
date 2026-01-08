# Time Complexity: O(max(m,n))
# Space Complexity: O(1)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LL:
    def addNums(self, l1, l2):
        dummy = Node(0)
        temp = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.value if l1 else 0
            v2 = l2.value if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            temp.next = Node(total % 10)
            temp = temp.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
    """
    def display(self, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")"""
"""
l1 = Node(2)
l1.next = Node(4)   
l1.next.next = Node(3)  # represents number 342
l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)  # represents number 465
ll = LL()
ll.display(l1)                         #2->4->3->None
ll.display(l2)                         #5->6->4->None
new_head = ll.addNums(l1, l2)
ll.display(new_head)                   #7->0->8->None (represents number 807)"""
