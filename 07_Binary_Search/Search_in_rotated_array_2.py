# Linear Search Approach
# Time Complexity: O(N)
# Space Complexity: O(1)
def rotated_2(nums, n, target):
    res = False
    for i in range(n):
        if nums[i] == target:
            res = True
    return res
print(rotated_2([2,5,6,0,0,1,2], 7, 0))
# True
print(rotated_2([2,5,6,0,0,1,2], 7, 3))
# False
print(rotated_2([1,0,1,1,1], 5, 0))
# True



# Binary Search Approach
# Time Complexity: O(LogN)
# Space Complexity: O(1)
def rotated_2(nums, n, target):
    low = 0 
    high = n - 1
    res = False
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            res = True
        if nums[low] == nums[mid] and nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue
        elif nums[low] <= nums[mid]:
            if nums[low] <= target and target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return res
print(rotated_2([2,5,6,0,0,1,2], 7, 0))
# True
print(rotated_2([2,5,6,0,0,1,2], 7, 3))
# False 
print(rotated_2([1,0,1,1,1], 5, 0))
# True

