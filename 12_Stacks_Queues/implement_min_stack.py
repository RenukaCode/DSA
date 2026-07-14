# Time Complexity: O(1)
# Space Complexity: O(n)
class MinStack:
    def __init__(self):
        self.st = []
    def push(self, x):
        if not self.st:
            self.st.append((x,x))
            return
        mini = min(self.getMin(), x)
        self.st.append((x, mini))
    def pop(self):
        self.st.pop()
    def top(self):
        return self.st[-1][0]
    def getMin(self):
        return self.st[-1][1]
    
if __name__ == "__main__":
    s = MinStack()
    
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin(), end=" ")
    s.pop()
    print(s.top(), end=" ")
    s.pop()
    print(s.getMin())
# -3 0 -2


# Time Complexity: O(1)
# Spqce Complexity: O(n)
class MinStack:
    def __init__(self):
        self.st = []
        self.mini = None
    def push(self, val):
        if not self.st:
            self.mini = val
            self.st.append(val)
            return 
        if val> self.mini:
            self.st.append(val)
        else:
            self.st.append(2*val-self.mini)
            self.mini = val
    def pop(self):
        if not self.st:
            return 
        x = self.st.pop()
        if x < self.mini:
            self.mini = 2*self.mini - x
    def top(self):
        if not self.st:
            return -1
        x = self.st[-1]
        if self.mini < x:
            return x
        return self.mini
    def getMin(self):
        return self.mini
    
if __name__ == "__main__":
    s = MinStack()

    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin(), end=" ")
    s.pop()
    print(s.top(), end=" ")
    s.pop()
    print(s.getMin())
# -3 0 -2