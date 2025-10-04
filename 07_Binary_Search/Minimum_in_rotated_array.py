# Linear Search Approach
# Time Complexity: O(N)
# Space Complexity: O(1)
def minEle(nums, n):
    res = float('inf')
    for i in range(n):
        if nums[i] < res:
            res = min(res, nums[i])
    return res
print(minEle([3,4,5,1,2], 5))
# 1
print(minEle([4,5,6,7,0,1,2], 7))
# 0
print(minEle([11,13,15,17], 4))
# 11



# Binary Search Approach
# Time Complexity: O(LogN)
# Space Complexity: O(1)
def minEle(nums, n):
    low = 0
    high = n - 1
    res = float('inf')
    while low <= high:
        mid = (low + high) // 2
        if nums[low] <= nums[mid]:
            res = min(res, nums[low])
            low = mid + 1
        else:
            res = min(res, nums[mid])
            high = mid - 1
    return res
print(minEle([3,4,5,1,2], 5))
# 1
print(minEle([4,5,6,7,0,1,2], 7))
# 0
print(minEle([11,13,15,17], 4))
# 11

def minEle(nums, n):
    low = 0
    high = n - 1
    res = float('inf')
    while low <= high:
        mid = (low + high) // 2
        if nums[low] <= nums[high]:
            res = min(res, nums[low])
            break
        if nums[low] <= nums[mid]:
            res = min(res, nums[low])
            low = mid + 1
        else:
            res = min(res, nums[mid])
            high = mid - 1
    return res
print(minEle([3,4,5,1,2], 5))  
# 1
print(minEle([4,5,6,7,0,1,2], 7))
# 0
print(minEle([11,13,15,17], 4))
# 11 
            