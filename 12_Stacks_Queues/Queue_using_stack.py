# Time Complexity: O(n)
# Space Complexity: O(n)
class StackQueue:
    def __init__(self):
        self.st1 = []
        self.st2 = []
    def push(self, x):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st1.append(self.st2.pop())
    def pop(self):
        if not self.st1:
            print("Stack is empty")
            return -1
        return self.st1.pop()
    def peek(self):
        if not self.st1:
            print("Stack is Empty")
            return -1
        return self.st1[-1]
    def isEmpty(self):
        return len(self.st1) == 0

if __name__ == "__main__":
    q = StackQueue()

    commands = ["StackQueue", "push", "push", "pop", "peek", "isEmpty"]
    inputs = [[], [4], [8], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            q.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "pop":
            print(q.pop(), end=" ")
        elif commands[i] == "peek":
            print(q.peek(), end=" ")
        elif commands[i] == "isEmpty":
            print("true" if q.isEmpty() else "false", end=" ")
        elif commands[i] == "StackQueue":
            print("null", end=" ")
# null null null 4 8 false 



# Time Complexity: O(1)
# Space Complexity: O(n)
class StackQueue:
    def __init__(self):
        self.input = []
        self.output = []
    def push(self, x):
        self.input.append(x)
    def pop(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        if not self.output:
            print("Queue is Empty")
            return -1
        return self.output.pop()
    def peek(self):
        if not self.output:
            print("Queue is Empty")
            return -1
        return self.output[-1]
    def isEmpty(self):
        return  not self.input and  not self.output

if __name__ == "__main__":
    q = StackQueue()
    q.push(3)
    q.push(4)
    print(q.pop(), end=" ")
    q.push(5)
    print(q.peek(), end = " ")
    print(q.isEmpty(), end = " ")
    print(q.pop(), end = " ")
    print(q.pop(), end = " ")
    print(q.isEmpty())
# 3 4 False 4 5 True
            