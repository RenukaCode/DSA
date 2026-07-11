# Time Complexity: O(1)
# Space Complexity: O(n)
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedListStack:
    def __init__(self):
        self.head  = None
        self.size = 0
    def push(self,x):
        ele = Node(x)
        ele.next = self.head
        self.head = ele
        self.size += 1
    def pop(self):
        if self.head is None:
            return -1
        value = self.head.val
        temp = self.head
        self.head = self.head.next
        del temp
        self.size -= 1
        return value
    def top(self):
        if self.head is None:
            return -1
        return self.head.val
    def isEmpty(self):
        return self.size == 0
    
st = LinkedListStack()
commands = ["LinkedListStack", "push", "push", "pop", "top", "isEmpty"]
inputs = [[], [3], [7], [], [], []]

for i in range(len(commands)):
    if commands[i] == "push":
        st.push(inputs[i][0])
        print("null", end=" ")
    elif commands[i] == "pop":
        print(st.pop(), end=" ")
    elif commands[i] == "top":
        print(st.top(), end=" ")
    elif commands[i] == "isEmpty":
        print("true" if st.isEmpty() else "false", end=" ")
    elif commands[i] == "LinkedListStack":
        print("null", end=" ")   
    
# null null null 7 3 false