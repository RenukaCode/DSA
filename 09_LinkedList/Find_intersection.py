# Brute Force Approach
# Time Complexity: O(m*n)
# Space Complexity: O(1)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def findIntersection(self, head1, head2):
        if not head1 or not head2:
            return None
        while head2:
            temp = head1
            while temp:
                if temp == head2:
                    return head2
                temp = temp.next
            head2 = head2.next
        return None
    def display(self, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")
"""
head = Node(3)
head.next = Node(1) 
head.next.next = Node(2)
head.next.next.next = Node(4)
head2 = head.next.next  # Node with value 2
ll = LL()
ll.display(head)                         #3->1->2->4->None
ll.display(head2)                        #2->4->None
intersection_node = ll.findIntersection(head, head2)
if intersection_node:
    print("Intersection at node with value:", intersection_node.value) 
    #Intersection at node with value: 2 """



# Better Approach using Hashing
# Time Complexity: O(m+n)
# Space Complexity: O(n)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def findIntersection(self, head1, head2):
        seen = set()
        while head1:
            seen.add(head1)
            head1 = head1.next
        while head2:
            if head2 in seen:
                return head2
            head2 = head2.next
        return None
    """
    def display(self, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")"""
"""
head = Node(3)
head.next = Node(1) 
head.next.next = Node(2)
head.next.next.next = Node(4)
head2 = head.next.next  # Node with value 2
ll = LL()
ll.display(head)                         #3->1->2->4->None
ll.display(head2)                        #2->4->None
intersection_node = ll.findIntersection(head, head2)
if intersection_node:
    print("Intersection at node with value:", intersection_node.value)""" 
    #Intersection at node with value: 2



# Optimal Approach
# Time Complexity: O(2 × max(length of list1, length of list2)) + O(abs(length of list1 − length of list2)) + O(min(length of list1, length of list2))
# Space Complexity: O(1)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def findDiff(self,head1, head2):
        len1, len2 = 0, 0
        temp1 = head1
        temp2 = head2
        while temp1:
            if head1:
                len1 += 1
                temp1 = temp1.next
            if head2:
                len2 += 1
                temp2 = temp2.next
        return len1 - len2
    def findIntersection(self, head1, head2):
        diff = self.findDiff(head1, head2)
        if diff < 0:
            diff = -diff
            while diff > 0:
                head2 = head2.next
                diff -= 1
        else:
            while diff > 0:
                head1 = head1.next
                diff -= 1
        while head1 and head2:
            if head1 is head2:
                return head1
            head2 = head2.next
            head1 = head1.next
        return None
    """
    def display(self, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")"""
"""
head = Node(3)
head.next = Node(1) 
head.next.next = Node(2)
head.next.next.next = Node(4)
head2 = head.next.next  # Node with value 2
ll = LL()
ll.display(head)                         #3->1->2->4->None
ll.display(head2)                        #2->4->None
intersection_node = ll.findIntersection(head, head2)
if intersection_node:
    print("Intersection at node with value:", intersection_node.value) 
    #Intersection at node with value: 2"""



# Optimal Approach(Two pointers)
# Time Complexity: O(m+n)
# Space Complexity: O(1)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def findIntersection(self, head1, head2):
        d1, d2 = head1, head2
        while d1 != d2:
            d1 = head2 if d1 is None else d1.next
            d2 = head1 if d2 is None else d2.next
        return d1
    """
    def display(self, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")"""
"""
head = Node(3)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(4)
head2 = head.next.next  # Node with value 2
ll = LL()
ll.display(head)                         #3->1->2->4->None
ll.display(head2)                        #2->4->None    
intersection_node = ll.findIntersection(head, head2)
if intersection_node:
    print("Intersection at node with value:", intersection_node.value) 
    #Intersection at node with value: 2"""