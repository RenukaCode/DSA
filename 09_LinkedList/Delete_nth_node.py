# Brute Force Approach
# Time Complexity: O(L)+O(L-N)
# Space Complexity: O(1)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def deleteNode(self, head, N):
        if head is None:
            return head.next
        Len = 0
        temp = head
        while temp:
            Len += 1
            temp = temp.next
        res = Len - N
        temp = head
        while temp:
            res -= 1
            if res == 0:
                break
            temp = temp.next
        temp.next = temp.next.next
        return head
    """
    def display(self, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")"""
"""
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
ll = LL()
ll.display(head)                         #1->2->3->4->5->None
new_head = ll.deleteNode(head, 2)
ll.display(new_head)                     #1->2->3->5->None"""



# Optimal Solution
# Time Complexity: O(N)
# Space Complexity: O(1)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def deleteNode(self, head, N):
        dummy = Node(0)
        dummy.next = head
        fast = slow = dummy
        for _ in range(N+1):
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
    """
    def display(self, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")"""
"""
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
ll = LL()
ll.display(head)                         #1->2->3->4->5->None
new_head = ll.deleteNode(head, 3)
ll.display(new_head)                     #1->2->4->5->None"""
