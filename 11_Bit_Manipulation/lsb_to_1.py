# Time Complexity: O(1)
# Space Complexity: O(1)
def fn(n):
    if n &1:
        return n
    return n|(n+1)
print(fn(5)) # 5
print(fn(10)) # 11
print(fn(7)) # 7