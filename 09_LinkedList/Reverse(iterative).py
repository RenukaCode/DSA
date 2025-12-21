# Time Complexity: O(N)
# Space Complexity: O(N)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LL:
    def reverse(self, head):
        stack = []
        temp = head
        while temp:
            stack.append(temp.value)
            temp = temp.next
        temp = head
        while temp:
            temp.value = stack.pop()
            temp = temp.next
        return head
    def display(self,head):
        temp = head
        while temp:
            print(temp.value, end = "->") 
            temp = temp.next
        print("None")
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
ll = LL()
ll.display(head)                   #1->2->3->4->None
ll.reverse(head)
ll.display(head)                   #4->3->2->1->None



# Time Complexity: O(N)
# Space Complexity: O(1)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LL:
    def reverse(self, head):
        node = None
    def __init__(self):
        self.head = None
        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp
        self.head = node
    def display(self):
        temp = self.head
        while temp:
            print(temp.value, end = "->")
            temp = temp.next
        print("None")
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
ll = LL()
ll.head = head
ll.display()                          #1->2->3->4->None
head = ll.reverse(ll.head)
ll.display()                          #4->3->2->1->None

