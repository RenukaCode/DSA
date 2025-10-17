# Brute Force Approach
# Time Complexity: O(N * (sum(arr[])-max(arr[])+1))
# Space Complexity: O(1)
def countPartitions(nums, maxSum):
    partitions = 1
    subarraySum = 0
    for i in range(len(nums)):
        if subarraySum + nums[i] <= maxSum:
            subarraySum += nums[i]
        else:
            partitions += 1
            subarraySum = nums[i]
    return partitions
def fn(nums, k):
    low = max(nums)
    high = sum(nums)
    for i in range(low, high + 1):
        if countPartitions(nums,i) == k:
            return i
    return low
print(fn([10, 20, 30, 40], 2))
# 60
print(fn([3,5,1], 3))
# 5
print(fn([10, 20, 30, 40],2))
# 60



# Optimal Solution
# Time Complexity: O(N * log(sum(arr[])-max(arr[])+1))
# Space Complexity: O(1)
def countPartitions(nums, maxSum):
    partitions = 1
    subarraySum = 0
    for i in range(len(nums)):
        if subarraySum + nums[i] <= maxSum:
            subarraySum += nums[i]
        else:
            partitions += 1
            subarraySum = nums[i]
    return partitions
def fn(nums, k):
    low = max(nums)
    high = sum(nums)
    res = low
    while low <= high:
        mid = (low + high) // 2
        if countPartitions(nums, mid) == k:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res
print(fn([10, 20, 30, 40], 2))
# 60
print(fn([3,5,1], 3))
# 5
print(fn([10, 20, 30, 40],2))
# 60
