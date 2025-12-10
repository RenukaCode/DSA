class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class Sol:
    def deleteNode(self, head):
        if head is None or head.next is None:
            return None
        curr = head
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None
        return head
    def display(self):
        temp = head
        while temp:
            print(temp.data, end = " ")        
            temp = temp.next
        print()
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
sol = Sol()
sol.display()          # 1 2 3
head = sol.deleteNode(head)
sol.display()          # 1 2



 