# Brute Force Approach
# Time Complexity: O(N)
# Space Complexity: O(N)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def starting(self, head):
        seen = set()
        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        return None
"""
head = Node(3)
head.next = Node(2)
head.next.next = Node(0)
head.next.next.next = Node(-4)
head.next.next.next.next = head.next
ll = LL()
startNode = ll.starting(head)
print(startNode.value)  """                 #2



# Optimal Approach
# Time Complexity: O(N)
# Space Complexity: O(1)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def starting(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
"""
head = Node(3)
head.next = Node(2)
head.next.next = Node(0)
head.next.next.next = Node(-4)
head.next.next.next.next = head.next
ll = LL()
startNode = ll.starting(head)
print(startNode.value) """               #2



