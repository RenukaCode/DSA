# Time Complexity: O(N)
# Space Complexity: O(1)
"""class Node:
    def __init__(self, val):
        self.val = val
        self.next = None"""
class LinkedList:
    def length(slef, head):
        temp = head
        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next
        return cnt
# Example usage:
"""head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
ll = LinkedList()
print(ll.length(head))    # Output: 3"""