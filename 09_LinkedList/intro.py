# creation of singly linkedlist
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
n1 = Node(5)
n2 = Node(15)
n3 = Node(25)
n1.next = n2
n2.next = n3
n3.next = None
print(n1.value)       #5
print(n2.value)       #15
print(n3.value)       #25
print(n1.next.value)  #15
print(n2.next.value)  #25   
print(n3.next)        #None

# print in ll format
temp = n1
while temp:
    print(temp.value, end = '->')
    temp = temp.next
print('None')
#5->15->25->None



# Insertion / adding of nodes
# 1. at head
# 2. at end
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def insert_at_end(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode 

    def delete_by_value(self, value):
        # 1. empty list
        if not self.head:
            return
        # 2. value at head
        if self.head.value == value:
            self.head = self.head.next
            return
        # 3. value in between or end
        temp = self.head
        while temp.next and temp.next.value != value:
            temp = temp.next
        # value not found
        if not temp.next:
            return
        # value found
        temp.next = temp.next.next
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.value, end = '->')
            temp = temp.next
        print('None')
ll = LinkedList()
ll.insert_at_head(10)
ll.insert_at_head(20)
ll.insert_at_head(30)
ll.insert_at_end(40)
ll.insert_at_end(50)
ll.display()
#30->20->10->40->50->None
ll.delete_by_value(10)
ll.display()
#30->20->40->50->None
ll.delete_by_value(30)
ll.display()
#20->40->50->None
ll.delete_by_value(100)   #not present, no change
ll.display()
#20->40->50->None

    
arr = [2,5,8,7]
y = Node(arr[0])
print(y)
print(y.value)