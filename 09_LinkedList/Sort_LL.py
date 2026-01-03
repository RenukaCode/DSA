# Brute Force Approach
# Time Complexity: O(2*N + N*LogN)
# Space Complexity: O(N)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def sortLL(self, head):
        arr = []
        temp = head
        while temp:
            arr.append(temp.value)
            temp = temp.next
        arr.sort()
        temp = head
        for val in arr:
            temp.value = val
            temp = temp.next
        return head
    """
    def display(self,head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")"""
"""
head = Node(4)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(3)
ll = LL()
ll.display(head)                         #4->2->1->3->None
new_head = ll.sortLL(head)
ll.display(new_head)                     #1->2->3->4->None"""



# Optimal Solution
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LL:
    def sortLL(self, head):
        if head is None or head.next is None:
            return head
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        left = self.sortLL(head)
        right = self.sortLL(slow)
        return self.mergeLL(left, right)
    def mergeLL(self, l1, l2):
        dummy = Node(0)
        temp = dummy
        while l1 and l2:
            if l1.value <= l2.value:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return dummy.next
    """
    def display(self, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")"""
"""
head = Node(4)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(3)
ll = LL()
ll.display(head)                         #4->2->1->3->None
new_head = ll.sortLL(head)
ll.display(new_head)                     #1->2->3->4->None
"""