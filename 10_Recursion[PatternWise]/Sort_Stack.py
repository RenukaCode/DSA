# Time Complexity: O(n^2)
# Space Complexity: O(n)
def insert(stack,temp):
    if not stack or stack[-1] <= temp:
        stack.append(temp)
        return
    val = stack.pop()
    insert(stack,temp)
    stack.append(val)
def sortStack(stack):
    if stack:
        temp = stack.pop()
        sortStack(stack)
        insert(stack,temp)
    return stack
stack = [34,3,31,98,92,23]
print(sortStack(stack) )