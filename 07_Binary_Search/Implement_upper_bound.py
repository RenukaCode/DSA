# Brute Force Approach
# Time Complexity: O(N)
# Space Complexity: O(1)
def upperBound(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] > target:
            return i
    return n
print(upperBound([3, 5, 8, 9, 15, 19], 9))
# 4 
print(upperBound([1,2,2,3], 2))
# 3
print(upperBound([0, 1, 2, 4, 4, 4, 5], 4))
# 6



# Optimal Approach
# Time Complexity: O(logN)
# Space COmplexity: O(1)
def upperBound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    res = n
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res
print(upperBound([3, 5, 8, 9, 15, 19], 9))
# 4
print(upperBound([1,2,2,3], 2))
# 3
print(upperBound([0, 1, 2, 4, 4, 4, 5], 4))
# 6