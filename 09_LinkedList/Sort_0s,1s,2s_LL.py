class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LL:
    def sortLL(self, head):
        zeroDummy = Node(-1)
        oneDummy = Node(-1)
        twoDummy = Node(-1)
        zeroTail = zeroDummy
        oneTail = oneDummy
        twoTail = twoDummy
        temp = head
        while temp:
            if temp.value == 0:
                zeroTail.next = temp
                zeroTail = zeroTail.next
            elif temp.value == 1:
                oneTail.next = temp
                oneTail = oneTail.next
            else:
                twoTail.next = temp
                twoTail = twoTail.next
            temp = temp.next
        zeroTail.next = oneDummy.next if oneDummy.next else twoDummy.next
        oneTail.next = twoDummy.next
        twoDummy.next = None
        return zeroDummy.next
    def display(self, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")
"""
head = Node(1)
head.next = Node(2)
head.next.next = Node(0)
head.next.next.next = Node(1)
head.next.next.next.next = Node(2)
ll = LL()
ll.display(head)                         #1->2->0->1->2->None
new_head = ll.sortLL(head)
ll.display(new_head)                     #0->1->1->2->2->None"""
