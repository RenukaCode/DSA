# Time Complexity: O(logN)
# Space Complexity: O(1)
def findFloor(nums, n, target):
    low = 0
    high = n - 1
    res = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= target:
            res = nums[mid]
            low = mid + 1
        else:
            high = mid - 1
    return res
def findCeil(nums, n, target):
    res = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            res = nums[mid]
            high = mid - 1
        else:
            low = mid + 1
    return res
def floorAndCeil(nums, n, target):
    f = findFloor(nums, n, target)
    c = findCeil(nums, n, target)
    return (f, c)
print(floorAndCeil([1, 2, 8, 10, 10, 12, 19], 7, 5))
# (2, 8)
print(floorAndCeil([1, 2, 8, 10, 10, 12, 19], 7, 20))
# (19, -1)
print(floorAndCeil([1, 2, 8, 10, 10, 12, 19], 7, 0))
# (-1, 1)
