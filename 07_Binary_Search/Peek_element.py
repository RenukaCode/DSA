# Brute Force Approach
# Time Complexity: O(N)
# Space Complexity: O(1)
def peekEle(nums, n):
    res = []
    for i in range(n):
        if (i == 0 or nums[i - 1] < nums[i]) and (i == n - 1 or nums[i] > nums[i + 1]):
            return i
        
    return -1
print(peekEle([1, 3, 20, 4, 1, 0], 6))
# 2    
print(peekEle([1, 2, 3, 4, 5], 5))
# 4
print(peekEle([5, 4, 3, 2, 1], 5))
# 0



# Optimal Approach
# Time Complexity: O(LogN)
# Space Complexity: O(1)
def peekele(nums, n):
    if n == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[n - 1] > nums[n - 2]:
        return n - 1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid] > nums[mid - 1]:
            low = mid + 1
        else:
            high = mid - 1
    return -1
print(peekele([1, 3, 20, 4, 1, 0], 6))
# 2
print(peekele([1, 2, 3, 4, 5], 5))
# 4
print(peekele([5, 4, 3, 2, 1], 5))
# 0

    