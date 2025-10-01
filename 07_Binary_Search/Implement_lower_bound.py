# Brute Force Approach
# Time Complexity: O(N)
# Space Complexity: O(1)
def lowerBound(nums, x):
    n = len(nums)
    for i in range(n):
        if nums[i] >= x:
            return i
    return n
print(lowerBound([3, 5, 8, 15, 19], 9))
# 3
print(lowerBound([1,2,2,3], 2))
# 1



# Optimal Solution
# Time Complexity: O(logN)
# Space Complexity: O(1)
def lowerBound(nums, x):
    n = len(nums)
    res = n
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= x:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res
print(lowerBound([3, 5, 8, 15, 19], 9))
# 3
print(lowerBound([1,2,2,3], 2))
# 1
print(lowerBound([0, 1, 2, 4, 4, 4, 5], 4))
# 3