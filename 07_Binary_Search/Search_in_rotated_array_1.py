# Linear Search Approach
# Time Complexity: O(N)
# Space Complexity: O(1)
def rotated_1(nums, n, target):
    res = -1
    for i in range(n):
        if nums[i] == target:
            res = i
    return res
print(rotated_1([4,5,6,7,0,1,2], 7, 0))
# 4 
print(rotated_1([4,5,6,7,0,1,2], 7, 3))
# -1



# Binary Search Approach
# Time Complexity: O(LogN)
# Space Complexity: O(1)
def rotated1(nums, n, target):
    low = 0
    high = n - 1
    res = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target and target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
print(rotated1([4,5,6,7,0,1,2], 7, 0))
# 4
print(rotated1([4,5,6,7,0,1,2], 7, 3))
# -1    
print(rotated1([1], 1, 1))
# 0

        