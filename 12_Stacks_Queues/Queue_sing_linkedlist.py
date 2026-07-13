class Node:
    def __init__(self, val):
        self.val = val
        self.next =None
class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,x):
        newNode = Node(x)
        if self.rear is None:
            self.front = self.rear = newNode
            return 
        self.rear.next = newNode
        self.rear = newNode
    def dequeue(self):
        if self.rear is None:
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.val
    def peek(self):
        if self.front is None:
            return None
        return self.front.val
    def isEmpty(self):
        return self.front is None
    def display(self):
        if self.front is None:
            return None
        curr = self.front
        while curr:
            print(curr.val, end = "->")
            curr = curr.next
        print("None")
q = LinkedListQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()       
print(q.dequeue())
print(q.peek())       
#10->20->30->None
10
20