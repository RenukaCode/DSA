# Linear Search Approach
# Time Complexity: O(N)
# Space Complexity: O(1)
def rotatedArray_count(nums, n):
    res = -1
    ans = float('inf')
    for i in range(n):
        ans = min(ans, nums[i])
        if nums[i] == ans:
            res = i
    return res
print(rotatedArray_count([15, 18, 2, 3, 6, 12], 6))
# 2
print(rotatedArray_count([7, 9, 11, 12, 5], 5))
# 4
print(rotatedArray_count([7, 9, 11, 12, 15], 5))
#  0



# Binary Search Approach
# Time Complexity: O(LogN)
# Space Complexity: O(1)
def rotatedArray_count(nums, n):
    low = 0
    high = n - 1
    ans = float('inf')
    res = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[low] <= nums[high]:
            ans = min(ans, nums[low])
            if nums[low] == ans:
                ans = nums[low]
                res = low
            break
        if nums[low] <= nums[mid]:
            ans = min(ans, nums[low])
            if nums[low] == ans:
                res = low
                ans = nums[low]
            low = mid + 1
        else:
            ans = min(ans, nums[mid])
            if nums[mid] == ans:
                res = mid
                ans = nums[mid]
            high = mid - 1
    return res
print(rotatedArray_count([15, 18, 2, 3, 6, 12], 6))
# 2
print(rotatedArray_count([7, 9, 11, 12, 5], 5))
# 4
print(rotatedArray_count([7, 9, 11, 12, 15], 5))
# 0