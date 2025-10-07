# Brute Force Approach 1
# Time Complexity: O(N)
# Space Complexity: O(1)
def singleEle(nums, n):
    ans = 0
    if n == 1:
        return nums[0]
    for i in range(n):
        if i == 0:
            if nums[i] != nums[i + 1]:
                ans = nums[i]
        elif i == n - 1:
            if nums[i] != nums[i - 1]:
                ans = nums[i]
        else:
            if nums[i] != nums[ i + 1] and nums[i] != nums[i - 1]:
                ans = nums[i]
    return ans
print(singleEle([1,1,2,3,3,4,4,8,8], 9))
# 2 
print(singleEle([3,3,7,7,10,11,11], 7))
# 10



# Brute Force Approach 2(XOR method)
# Time Complexity: O(N)
# Space Complexity: O(1)
def singleEle(nums, n):
    ans = 0
    for i in range(n):
        ans = ans ^ nums[i]
    return ans
print(singleEle([1,1,2,3,3,4,4,8,8], 9))
# 2
print(singleEle([3], 1))
# 3
print(singleEle([2,1,2], 3))
# 1



# Optimal Approach(Binary Search)
# Time Complexity: O(LogN)
# Space Complexity: O(1)
def singelEle(nums, n):
    low = 0
    high = n - 1
    if n == 1:
        return nums[0]
    elif nums[0] != nums[1]:
        return nums[0]
    elif nums[n - 1] != nums[n - 2]:
        return nums[n - 1]
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]
        elif (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
            low = mid + 1
        else:
            high = mid - 1
    return -1
print(singelEle([1,1,2,3,3,4,4,8,8], 9))    
# 2
print(singelEle([1], 1))
# 1
print(singelEle([1,1,2], 3))
# 2
print(singelEle([[1,1,2,3,3,4,4,8,8]], 9))