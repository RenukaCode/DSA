# Time Complexity: O(1)
# Space Complexity: O(1)
class Queue:
    def __init__(self):
        self.arr = [0]*10
        self.start = -1
        self.end = -1
        self.currSize = 0
        self.maxSize = 10
    def push(self,x):
        if self.currSize == self.maxSize:
            print("Queue is full")
            exit(1)
        if self.end == -1:
            self.start = 0
            self.end = 0
        else:
            self.end = (self.end + 1)% self.maxSize
        self.arr[self.end] = x
        self.currSize += 1
    def pop(self):
        if self.start == -1:
            print("Queue is empty")
            exit(1)
        popped = self.arr[self.start]
        if self.currSize == 1:
            self.start = -1
            self.end = -1
        else:
            self.start = (self.start+1)%self.maxSize
        self.currSize -= 1
        return popped
    def peek(self):
        if self.start == -1:
            print("Queue is Empty")
            exit(1)
        return self.arr[self.start]
    def isEmpty(self):
        return self.currSize == 0
    
if __name__ == "__main__":
    queue = Queue()
    commands = ["ArrayQueue", "push", "push", "peek", "pop", "isEmpty"]
    inputs = [[], [5], [10], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            queue.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "pop":
            print(queue.pop(), end=" ")
        elif commands[i] == "peek":
            print(queue.peek(), end=" ")
        elif commands[i] == "isEmpty":
            print("true" if queue.isEmpty() else "false", end=" ")
        elif commands[i] == "ArrayQueue":
            print("null", end=" ")
# null null null 5 5 false



