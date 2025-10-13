# Brute Force Approach
# Time Complexity: O(N)
# Space Complexity: O(1)
def fn(vec, k):
    n = len(vec)
    for i in range(n):
        if vec[i] <= k:
            k += 1
        else:
            break
    return k
print(fn([4,7,9,10], 1))
# 1
print(fn([4,7,9,10],4))
# 5



# Optimal Solution
# Time Complexity: O(LogN)
# Space Complexity: O(1)
def fn(vec, k):
    n = len(vec)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        missing = vec[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    return k + high + 1
print(fn([4,7,9,10], 1))
# 1
print(fn([4,7,9,10],4))
# 5
