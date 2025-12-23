# Brute Force Approach
# Time Complexity: O(N)
# Space Complexity: O(N)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def lengthll(self, head):
        self.head = None
        temp = head
        visited = {}
        timer = 0
        while temp is not None:
            if temp in visited:
                loopLength = timer - visited[temp]
                return loopLength
            visited[temp] = timer
            temp = temp.next
            timer += 1
        return 0
"""
head = Node(3)
head.next = Node(2)
head.next.next = Node(0)
head.next.next.next = Node(-4)
head.next.next.next.next = head.next
ll = LL()
print(ll.lengthll(head))"""
# 3
