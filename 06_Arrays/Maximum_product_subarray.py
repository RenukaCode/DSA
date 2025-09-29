# Brute Force Approach
# Time Complexity: O(N^3)
# Space Complexity: O(1)
def maxProductSubarray(nums, n):
    res = float('-inf')
    for i in range(n):
        for j in range(i + 1, n):
            prod = 1
            for k in range(i, j + 1):
                prod *= nums[k]
            res = max(res, prod)
    return res
print(maxProductSubarray([6, -3, -10, 0, 2], 5))
# 180   
print(maxProductSubarray([1,2,3,4,5,0], 6))
# 120
print(maxProductSubarray( [1,2,-3,0,-4,-5], 6))



# Better Approach
# Time Complexity: O(N^2)
# Space Complexity: O(1)
def maxProductSubarray(nums, n):
    res = nums[0]
    for i in range(n):
        prod = nums[i]
        for j in range(i + 1, n):
            res = max(res, prod)
            prod *= nums[j]
            res = max(res, prod)
    return res
print(maxProductSubarray([6, -3, -10, 0, 2], 5))
# 180
print(maxProductSubarray([1,2,3,4,5,0], 6))
# 120
print(maxProductSubarray( [1,2,-3,0,-4,-5], 6))
# 20



# Optimal Approach
# Time Complexity: O(N)
# Space Complexity: O(1)
def maxProductSubarray(nums, n):
    pref = 1
    suff = 1
    res = float('-inf')
    for i in range(n):
        if pref == 0:
            pref = 1
        if suff == 0:
            suff = 1
        pref *= nums[i]
        suff *= nums[n - i - 1]
        res = max(res, max(pref, suff))
    return res
print(maxProductSubarray([6, -3, -10, 0, 2], 5))
# 180
print(maxProductSubarray([1,2,3,4,5,0], 6))
# 120
print(maxProductSubarray( [1,2,-3,0,-4,-5], 6))
# 20



# Optimal Approach 2
# Time Complexity: O(N)
# Space Complexity: O(1)
def maxProductSubarray(nums, n):
    prod1 = nums[0]
    prod2 = nums[0]    
    res = nums[0]
    for i in range(1, n):
        temp = max(nums[i], prod1 * nums[i], prod2 * nums[i])
        prod2 = min(nums[i], prod1 * nums[i], prod2 * nums[i])
        prod1 = temp
        res = max(res, prod1)
    return res
print(maxProductSubarray([6, -3, -10, 0, 2], 5))
# 180   
print(maxProductSubarray([1,2,3,4,5,0], 6))
# 120   
print(maxProductSubarray( [1,2,-3,0,-4,-5], 6))
# 20        