# Time Complexity : O(logN)
def binarySearch(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
print(binarySearch([3, 4, 6, 7, 9, 12, 16, 17], 6))
#  2
print(binarySearch([3, 4, 6, 7, 9, 12, 16, 17], 10))
# -1



# Recursive Approach
# Time Complexity: O(logN)
def binarySearch(nums, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binarySearch(nums, target, low, mid - 1)
    else:
        return binarySearch(nums, target, mid + 1, high)
print(binarySearch([3, 4, 6, 7, 9, 12, 16, 17], 6, 0, 7))
#  2
print(binarySearch([3, 4, 6, 7, 9, 12, 16, 17], 10, 0, 7))
# -1
