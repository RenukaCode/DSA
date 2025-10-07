# Brute Force Approach
# Time Complexity: O(N)
# Space Complexity: O(1)
def floorSqrt(n):
    res = 0
    for i in range(1, n + 1):
        val = i * i
        if val <= n:
            res = i
        else:
            break
    return res
print(floorSqrt(36))
# 6
print(floorSqrt(28))
# 5



# Optimal Approach 1
# Time Complexity: O(LogN)
# Space Complexity: O(1)
import math
def floorSqrt(n):
    res = int(math.sqrt(n))
    return res
print(floorSqrt(36))
# 6
print(floorSqrt(28))
# 5



# Optimal Approach 2(Binary Search)
# Time Complexity: O(LogN)
# Space Complexity: O(1)
def floorSqrt(n):
    low = 0
    high = n 
    res = 0
    while low <= high:
        mid = (low + high) // 2
        val = mid * mid
        if val <= n:
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return res
print(floorSqrt(36))
# 6
print(floorSqrt(28))    
# 5
