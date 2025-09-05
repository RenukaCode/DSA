# link:  https://leetcode.com/problems/two-sum/


# Brute Force Approach
# Time Complexity: O(N^2)
# Space Complexity: O(1)
def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [-1, -1]
print(two_sum([2, 6, 5, 8, 11], 14))
# output: [1, 3]



# Using Hashing
# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum(nums, target):
    res = {}
    for i in range(len(nums)):
        j = target - nums[i]
        if j in res:
            return [res[j], i]
        res[nums[i]] = i
    return []
print(two_sum([11, 15, 2, 7], 9))  
# o/p : [2, 3]
print(two_sum([11, 15], 9))
# o/p : []



# Two pointers Approach
# Time Complexity: O(N) + O(N*logN)
# Space Complexity: O(N)
def two_sum(nums, target):
    n = len(nums)
    num = sorted(nums)
    left = 0
    right = n - 1
    while left < right:
        if num[left] + num[right] == target:
            return [left, right]
        elif num[left] + num[right] > target:
            right -= 1
        else:
            left += 1
    return [-1, -1]
print(two_sum([11, 15, 2, 7], 9))
# output: [0, 1]
print(two_sum([2, 6, 5, 8, 11], 14))
# output: [2, 3]
