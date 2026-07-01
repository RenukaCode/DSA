# Time Complexity: O(1)
# Space Complexity: O(1)
def fn(n):
    return n > 1 and (n&(n-1)) == 0
print(fn(16)) # True
print(fn(5)) # False