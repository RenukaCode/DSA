# Time Complexity: O(n)
# Space Complexity: O(1)
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertAtEnd(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
    def display(self):
        temp = self.head
        while temp:
            print(temp.value, end = " <-> ")
            temp = temp.next
        print("None")
# Example usage:
dll = DLL()
dll.insertAtEnd(10)
dll.insertAtEnd(20)
dll.insertAtEnd(30)
dll.display()    # 10 <-> 20 <-> 30 <-> None
dll.insertAtEnd(40)
dll.display()    # 10 <-> 20 <-> 30 <-> 40 <-> None