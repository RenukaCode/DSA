# Brute Force Approach
# Time Complexity: O(N*N)
# Space Complexity: O(1)
import math
def fn(arr, limit):
    n = len(arr)
    if n > limit:
        return -1
    maxi = max(arr)
    for d in range(1, maxi + 1):
        sum_ = 0
        for i in range(n):
            sum_ += math.ceil(arr[i] / d)
        if sum_ <= limit:
            return d
    return -1
print(fn([1,2,3,4,5], 8))
# 3
print(fn([8,4,2,3],10))
# 2



# Optimal Solution
# Time Complexity: O(LogN)
# Space Complexity: O(1)
def fn(arr, limit):
    high = max(arr)
    low = 1
    res = -1
    while low <= high:
        mid = (low + high) // 2
        sum_ = 0
        for i in arr:
            sum_ += math.ceil(i / mid)
        if sum_ <= limit:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res
print(fn([1,2,3,4,5], 8))
# 3
print(fn([8,4,2,3],10))
# 2

