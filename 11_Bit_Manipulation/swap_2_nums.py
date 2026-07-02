# Time Complexity: O(1)
# Space Complexity: O(1)
def fn(num1,num2):
    num1 = num1^num2
    num2 = num1^num2
    num1 = num1^num2
    return num1,num2
print(fn(5,10)) # (10, 5)
print(fn(7,3)) # (3, 7)