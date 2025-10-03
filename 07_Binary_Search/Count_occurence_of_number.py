# Linear Search Approach
# Time Compelxity: O(N)
# Space Complexity: O(1)
def occurence(nums, n, target):
    count = 0
    for i in range(n):
        if nums[i] == target:
            count += 1
    return count
print(occurence([1, 2, 2, 2, 3, 4, 5], 7, 2))
# 3 
print(occurence([3,4,13,13,13,13,20,40], 7, 13))
# 4
print(occurence([1,1,1,1,1], 5, 1))
# 5
print(occurence([1,2,3,4,5], 5, 6))
# 0




# Binary Search Approach
# Time Complexity: O(2*LogN)
# Space Complexity: O(1)
def firstOccurence(nums, n, target):
    res = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            res = mid
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return res
def lastOccurence(nums, n, target):
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
def countOccurence(nums, n, target):
    first = firstOccurence(nums, n, target)
    last = lastOccurence(nums, n, target)
    if first == -1 or last == -1:
        return 0
    return last - first + 1
print(countOccurence([1, 2, 2, 2, 3, 4, 5], 7, 2))
# 3
print(countOccurence([3,4,13,13,13,13,20,40], 7, 13))
# 4
print(countOccurence([1,1,1,1,1], 5, 1))
# 5
print(countOccurence([1,2,3,4,5], 5, 6))
# 0