# Time Complexity: O(1)
# Space Complexity: O(n)
class ArrayStack:
    def __init__(self, size = 1000):
        self.stackArr = [0]*size
        self.capacity = size
        self.topIdx = -1
    def push(self,x):
        if self.topIdx >= self.capacity-1:
            print("Stack Overflow")
            return
        self.topIdx += 1
        self.stackArr[self.topIdx] = x
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return -1
        topEle = self.stackArr[self.topIdx]
        self.topIdx -= 1
        return topEle
    def top(self):
        if self.isEmpty():
            print("Stack is Empty")
            return -1
        return self.stackArr[self.topIdx]
    def isEmpty(self):
        return self.topIdx == -1
    
if __name__ == "__main__":
    stack = ArrayStack()
    commands = ["ArrayStack", "push", "push", "top", "pop", "isEmpty"]
    inputs = [[], [5], [10], [], [], []]
    for i in range(len(commands)):
        if commands[i] == "push":
            stack.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "pop":
            print(stack.pop(), end=" ")
        elif commands[i] == "top":
            print(stack.top(), end=" ")
        elif commands[i] == "isEmpty":
            print("true" if stack.isEmpty() else "false", end=" ")
        elif commands[i] == "ArrayStack":
            print("null", end=" ")
# null null null 10 10 false 