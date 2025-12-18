# node = None
# temp = head.next
# head.next = node
# head.prev = temp
# node = head
# head = temp
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
class DLL:
    def __init__(self):
        self.head = None
    def reverse(self):
        temp = self.head
        last = None
        while temp:
            temp.prev, temp.next = temp.next, temp.prev
            last = temp
            temp = temp.prev
        self.head =last

    def display(self):
        temp = self.head
        while temp:
            print(temp.value, end = " <-> ")
            temp = temp.next
        print("None")
# Example usage:
dll = DLL()
dll.head = Node(10)
n2 = Node(20)
n3 = Node(30)
dll.head.next = n2
n2.prev = dll.head
n2.next = n3
n3.prev = n2
dll.display()    # 10 <-> 20 <-> 30 <-> None
dll.reverse()
dll.display()    # 30 <-> 20 <-> 10 <-> None