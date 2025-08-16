# link: https://leetcode.com/problems/maximum-subarray/

#Kadane's formula
def maxSub(nums):
    curr = nums[0]
    maxCurr = nums[0]
    for i in range(1, len(nums)):
        curr = max(nums[i], nums[i] + curr)
        maxCurr = max(maxCurr, curr)
    return maxCurr

# example:
print(maxSub([-2,1,-3,4,-1,2,1,-5,4])) # o/p: 6
# time complexity: O(n)
# space complexity: O(1)

#or

def maxSubArray(nums):
    res = nums[0]
    total = 0
    for n in nums:
        if total < 0:
            total = 0
        total += n
        res = max(res, total)
    return res

# example:
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # o/p: 6  

# Time Complexity: O(n)
# Space Complexity: O(1)
