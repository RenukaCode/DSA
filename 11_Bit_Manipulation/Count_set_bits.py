# Brute Force Approach
# Time Complexity: O(log n)
# Space Complexity: O(1)
def fn(n):
    cnt = 0
    while n > 0:
        cnt += n&1
        n >>= 1
    return cnt
print(fn(5)) # 2
print(fn(16)) # 1
print(fn(7)) # 3



# Optimal Approach
# Time Complexity: O(k), where k is the number of set bits in n
# Space Complexity: O(1)
def fn(n):
    cnt = 0
    while n > 0:
        n &= n-1
        cnt += 1
    return cnt
print(fn(5)) # 2
print(fn(16)) # 1
print(fn(7)) # 3