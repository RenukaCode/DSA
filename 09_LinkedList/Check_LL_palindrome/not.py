# Brute Force Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def palindrome(self, head):
        temp = head
        stack = []
        while temp is not None:
            stack.append(temp.value)
            temp = temp.next
        temp = head
        while temp is not None:
            if temp.value != stack.pop():
                return False
            temp =temp.next
        return True
    def display(self, head):
        temp = head
        while temp:
            print(temp.value, end = "->")
            temp =temp.next
        print("None")
"""
head = Node(1)
head.next = Node(5)
head.next.next = Node(2)
head.next.next.next = Node(5)
head.next.next.next.next = Node(1)
ll = LL()
ll.display(head)                         #1->5->2->5->1->None
print(ll.palindrome(head))               #True
""" 



# Optimal Approach 
# Time Complexity: O(N)
# Space Complexity: O(1)
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None"""
class LL:
    def __init__(self):
        self.left = None
    def palindrome(self, head):
        self.left = head
        return self.check(head)
    def check(self, right):
        if right is None:
            return True
        if not self.check(right.next):
            return False
        if self.left.value != right.value:
            return False
        self.left = self.left.next
        return True
"""
head = Node(1)
head.next = Node(5)
head.next.next = Node(2)
head.next.next.next = Node(5)
head.next.next.next.next = Node(1)

ll = LL()
print(ll.palindrome(head))  # True"""


