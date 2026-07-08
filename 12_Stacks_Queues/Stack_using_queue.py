# Time Complexity: O(n)
# Space Complexity: O(1)
from queue import Queue
class ArrQueue():
    def __init__(self):
        self.q = Queue()
    def push(self, x):
        s = self.q.qsize()
        self.q.put(x)
        for _ in range(s):
            self.q.put(self.q.get())
    def pop(self):
        n = self.q.queue[0]
        self.q.get()
        return n
    def top(self):
        return self.q.queue[0]
    def isEmpty(self):
        return self.q.empty()
    
if __name__ == "__main__":
    st = ArrQueue()
    commands = ["QueueStack", "push", "push", "pop", "top", "isEmpty"]
    inputs = [[], [4], [8], [], [], []]

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
        elif commands[i] == "QueueStack":
            print("null", end=" ")
# null null null 8 4 false 
