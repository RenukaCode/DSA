# Time Complexity: O(1)
# Space Complexity: O(1)
class Node:
    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1
class LinkedList:
    def insertAtHead(self, head, newData):
        newData = Node(newData, head)
        return newData
    def printList(self, head):
        temp = head
        while temp:
            print(temp.data, end = "->")
            temp = temp.next
        print("None")
li = LinkedList()
head = Node(2)
head.next = Node(3)
print("Before Insertion at head: ")  #2->3->None
li.printList(head)
head = li.insertAtHead(head, 1)
print("After Insertion at head: ")   #1->2->3->None
li.printList(head)


