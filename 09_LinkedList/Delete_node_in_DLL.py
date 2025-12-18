class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
class DLL:
    def __init__(self):
        self.head = None
    def deleteNode(self):
        if not self.head:
            return None
        if not self.head.next:
            self.head = None
            return None
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None
        return self.head
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
dll.deleteNode()
dll.display()    # 10 <-> 20 <-> None

