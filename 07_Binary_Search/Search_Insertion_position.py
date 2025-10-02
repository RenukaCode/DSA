# Time Complexity: O(logN)
# Space Complexity: O(1)
def position(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    res = n
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res
print(position([1, 3, 5, 6], 5))
# 2
print(position([1, 3, 5, 6], 2))
# 1
print(position([1, 3, 5, 6], 7))
# 4
        