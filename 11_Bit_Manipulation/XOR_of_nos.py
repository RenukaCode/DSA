# Time Complexity: O(n)
# Space Complexity: O(1)
def fn(L,R):
    res = 0
    for i in range(L,R+1):
        res ^= i
    return res
print(fn(1,3)) # 0
print(fn(3,5)) # 2