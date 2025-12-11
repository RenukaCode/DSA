# Time Complexity: O(N)
# Space Complexity: O(1)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class Search:
    def searchEle(self, head, val):
        while head:
            if head.val == val:
                return True
            else:
                head = head.next
        return False
# Example usage:
"""
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
search = Search()
print(search.searchEle(head, 20))    # Output: True
print(search.searchEle(head, 40))    # Output: False"""