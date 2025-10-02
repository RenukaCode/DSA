def occurence(nums, n, target):
    res = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            res = mid
            low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return res
print(occurence([1, 2, 2, 2, 3, 4, 5], 7, 2))
# 3
print(occurence([3,4,13,13,13,20,40], 7, 13))  
# 4
print(occurence([1,1,1,1,1], 5, 1))
# 4

