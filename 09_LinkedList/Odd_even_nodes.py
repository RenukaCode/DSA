# Time Complexity: O(N)
# Space Complexity: O(1)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def seggregate(self, head):
        if head is None or head.next is None:
            return head
        evenHead = evenTail = None
        oddHead = oddTail = None
        temp = head
        while temp:
            if temp.value % 2 == 0:
                if not evenHead:
                    evenHead = evenTail = temp
                else:
                    evenTail.next = temp
                    evenTail = temp
            else:
                if not oddHead:
                    oddHead = oddTail = temp
                else:
                    oddTail.next = temp
                    oddTail = temp
            temp = temp.next
        if not oddHead:
            evenTail.next = None
            return evenHead
        if not evenHead:
            oddTail.next = None
            return oddHead
        oddTail.next = evenHead
        evenTail.next = None
        return oddHead
    """
    def display(self, head):
        temp = head
        while temp:
            print(temp.value, end = "->")
            temp = temp.next
        print("None")"""
"""
head = Node(1)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
ll = LL()
ll.display(head)                         #1->4->3->2->5->6->None
new_head = ll.seggregate(head)
ll.display(new_head)                     #4->2->6->1->3->5->None"""



# Time Complexity: O(N)
# Space Complexity: O(1)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None"""
class LL:
    def seggregate(self, head):
        odd, even = head, head.next
        evenHead = even
        if not head or not head.next:
            return head
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = evenHead
        return head
"""
    def display(self, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")"""
"""
head = Node(1)
head.next = Node(4)
head.next.next = Node(3)    
head.next.next.next = Node(2)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
ll = LL()
ll.display(head)                         #1->4->3->2->5->6->None
new_head = ll.seggregate(head)
ll.display(new_head)                     #1->3->5->4->2->6->None"""