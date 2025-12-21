# Brute Force Approach(Using hashmap)
# Time Complexity: O(N*LogN)
# Space Complexity: O(N)
"""class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def detect(self, head):
        nodeMap = {}
        temp = head
        while temp is not None:
            if temp in nodeMap:
                return True
            nodeMap[temp] = 1
            temp = temp.next
        return False
"""head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
ll = LL()
print(ll.detect(head))                  # False
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = third
ll = LL()
print(ll.detect(head))             #True"""



# Optimal Approach(Tortoise & Fare Approach)
# Time Complexity: O(N)
# Space Complexity: O(1)
"""class Node:
    def __init__(self, value):
        self.value = value
        self.next = next"""
class LL:
    def detect(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
"""head = Node(1)
second = Node(2)
third = Node(3)
fourth= Node(4)
fifth = Node(5)
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = None
ll = LL()
print(ll.detect(head))           #False
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = third
ll = LL()
print(ll.detect(head))         # True"""
        
        


