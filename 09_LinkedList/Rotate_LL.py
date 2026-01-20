# # Brute Force Approach
# # Time Complexity: O(n*k)
# # Space Complexity: O(1)
# """
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None"""
# class LL:
#     def rotate(self,head,k):
#         if not head or k == 0:
#             return head
#         for _ in range(k):
#             curr = head
#             prev = None
#             while curr.next:
#                 prev = curr
#                 curr = curr.next
#             prev.next = None
#             curr.next = head
#             head = curr
#         return head
#     """
#     def display(self, head):
#         while head:
#             print(head.value, end = "->")
#             head = head.next
#         print("None")"""
# """
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
# ll = LL()
# ll.display(head)                     #1->2->3->4->5->None
# new_head = ll.LL(head, 2)
# ll.display(new_head)                 #4->5->1->2->3->None
# """
    


# Optimal Solution 
# Time Complexity: O(N)
# Space Complexity: O(1)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def rotate(self, head, k):
        if not head or k == 0:
            return head
        temp = head
        length = 1
        while temp.next:
            temp = temp.next
            length += 1      
        temp.next = head
        k = k % length
        steps = length - k
        temp = head
        for _ in range(steps-1):
            temp = temp.next
        newHead = temp.next
        temp.next = None
        return newHead
"""
   def display(self, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")"""
"""head = Node(1)
head.next = Node(2) 
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
ll = LL()
ll.display(head)                     #1->2->3->4->5->None
new_head = ll.rotate(head, 7)
ll.display(new_head)                 #4->5->1->2->3->None"""
