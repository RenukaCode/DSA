# Time Complexity: O(n^2)
# Space Complexity: O(n)
def insertAtBottom(stack,val):
    if not stack:
        stack.append(val)
        return
    topVal = stack.pop()
    insertAtBottom(stack,val)
    stack.append(topVal)
def reverseStack(stack):
    if not stack:
        return
    topVal = stack.pop()
    reverseStack(stack)
    insertAtBottom(stack,topVal)
    return stack
stack = [1,2,3,4,5]
print(reverseStack(stack))    #[5, 4, 3, 2, 1]
