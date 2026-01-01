# Brute Force Approach
# Time Complexity: O(N+N/2)
# Space Complexity: O(1)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def deleteNode(self, head):
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        res = n // 2
        temp = head
        while temp is not None:
            res -= 1
            if res == 0:
                temp.next = temp.next.next
                break
            temp = temp.next
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
new_head = ll.deleteNode(head)
ll.display(new_head)                     #1->2->4->5->None"""




# Optimal Approach 
# Time Complexity: O(N/2)
# Space Complexity: O(1)

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def deleteNode(self, head):
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next
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
new_head = ll.deleteNode(head)
ll.display(new_head)                     #1->2->4->5->None"""
            