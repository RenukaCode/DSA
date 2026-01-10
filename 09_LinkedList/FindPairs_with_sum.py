# # BruteForce Approach
# # Time Complexity: O(n^2)
# # Space Complexity: O(1)
# """
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None"""
# class LL:
#     def findPairs(self, head, target):
#         res = []
#         temp1 = head
#         while temp1:
#             temp2 = temp1.next
#             while temp2:
#                 if temp1.value + temp2.value == target:
#                     res.append((temp1.value, temp2.value))
#                 temp2 = temp2.next
#             temp1 = temp1.next
#         return res
# """
#     def display(self, head):
#         while head:
#             print(head.value, end = "->")
#             head = head.next
#         print("None")
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
# ll = LL()
# ll.display(head)                     #1->2->3->4->5->None
# result = ll.findPairs(head, 5)
# print(result)                        #[(1,4),(2,3)]
# """



# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def findPairs(self, head, target):
        seen = set()
        res = []
        temp = head
        while temp:
            another = target - temp.value
            if another in seen:
                res.append((another, temp.value))
                seen.remove(another)
            else:
                seen.add(temp.value)
            temp = temp.next
        return res
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
ll.display(head)                     #1->2->3->4->5->None
result = ll.findPairs(head, 5)
print(result)                        #[(2,3),(1,4)]"""
