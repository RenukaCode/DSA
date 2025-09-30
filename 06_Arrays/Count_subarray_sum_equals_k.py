# Brute Force Approach
# Time Complexity: O(N^3)
# Space complexity: O(1)
def subarray(nums, k):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i, n):
            subarray_sum = sum(nums[i:j + 1])
            if subarray_sum == k:
                count += 1
    return count
print(subarray([3,1,2,4], 6))
#  output: 2  ([3,1,2] and [2,4])
print(subarray([1,2,3], 3))
# output: 2   ([1,2] and [3])



# Better Solution
# Time Complexity: O(N^2)
# Space Complexity: O(1)
def subarray(nums, k):
    n = len(nums)
    count = 0
    for i in range(n):
        subarray_sum = 0
        for j in range(i, n):
            subarray_sum += nums[j]
            if subarray_sum == k:
                count += 1
    return count
print(subarray([3,1,2,4], 6))
#  output: 2  ([3,1,2] and [2,4])
print(subarray([1,2,3], 3))
# output: 2   ([1,2] and [3])



# Optimal Approach(Using sliding window)
# Time Complexity: O(N)
# Space Complexity: O(1)
#  This method holds only for positive elements
def subarray(nums, k):
    n = len(nums)
    left = 0 
    subarray_sum = 0
    count = 0
    for right in range(n):
        subarray_sum += nums[right]
        while subarray_sum > k and left <= right:
            subarray_sum -= nums[left]
            left += 1
        if subarray_sum == k:
            count += 1
    return count
print(subarray([3,1,2,4], 6))
#  output: 2  ([3,1,2] and [2,4])
print(subarray([1,2,3], 3))
# output: 2   ([1,2] and [3])
            


# Optimal Solution 2
# Time Complexity: O(N)
# Space Complexity: O(N)
def subarray(nums, k):
    prefix_sum = 0
    n = len(nums)
    count = 0
    mp = {0:1}
    for i in range(n):
        prefix_sum += nums[i]
        if (prefix_sum - k) in mp:
            count += mp[prefix_sum- k]
        if prefix_sum in mp:
            mp[prefix_sum] += 1
        else:
            mp[prefix_sum] = 1
    return count
print(subarray([3,1,2,4], 6))
#  output: 2  ([3,1,2] and [2,4])
print(subarray([1,2,3], 3))
# output: 2   ([1,2] and [3])
