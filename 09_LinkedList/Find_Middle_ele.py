# BruteForce Approach
# Time Complexity: O(N+N/2)
# Space Complexity: O(1)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def mid_ele(self,head):
        if head is None or head.next is None:
            return head
        temp = head
        cnt = 0
        while temp is not None:
            cnt += 1
            temp = temp.next
        mid = (cnt // 2) + 1
        temp = head
        for _ in range(1, mid):
            temp = temp.next
        return temp
# Example usage:
"""
ll = LL()
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
mid = ll.mid_ele(head)
print("Mid element:", mid.value)     #30"""



# Optimal Approach
# Time Complexity: O(N/2)
# Space Complexity: O(1)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def midEle(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.value
# Example usage:
"""
ll = LL()
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
midele = ll.midEle(head)
print(midele)                       30""" 




