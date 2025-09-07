# link: https://leetcode.com/problems/maximum-subarray/

# Brute Force Approach
# Time Complexity O(N^3)
# Space Complexity: O(1)
def maxSub(nums):
    n = len(nums)
    maxSum = 0
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j + 1):
                sum += nums[k]
            maxSum = max(maxSum, sum)
    return maxSum
print(maxSub([-2,1,-3,4,-1,2,1,-5,4]))
#  output: 6



# Better Approach
# TIme Complexity: O(N^2)
# Space COmplexity: O(1)
def maxSub(nums):
    n = len(nums)
    maxSum = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            maxSum = max(maxSum, sum)
    return maxSum
print(maxSub([-2,1,-3,4,-1,2,1,-5,4]))
#  output: 6



# Optimal Solution
# Time Complexity: O(N)
# Space Complexoty: O(1)
def maxSub(nums):
    n = len(nums)
    maxSum = 0
    sum = 0
    for i in range(n):
        sum += nums[i]

        if sum < 0:
            sum = 0
        if sum > maxSum:
            maxSum = sum
    return maxSum
print(maxSub([-2,1,-3,4,-1,2,1,-5,4]))
#  output: 6



#Kadane's formula
# time complexity: O(n)
# space complexity: O(1)
def maxSub(nums):
    curr = nums[0]
    maxCurr = nums[0]
    for i in range(1, len(nums)):
        curr = max(nums[i], nums[i] + curr)
        maxCurr = max(maxCurr, curr)
    return maxCurr
print(maxSub([-2,1,-3,4,-1,2,1,-5,4])) 
# o/p: 6



