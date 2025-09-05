# Brute FOrce Approach
# Time Complexity: O(N^3)
# Space Complexity: O(1)
def subarray(arr, k):
    max_len = 0
    for i in arr:
        for j in range(i, len(arr)):
            total = sum(arr[i:j + 1])
            if total == k:
                max_len = max(max_len, len(arr[i:j + 1]))
    return max_len
print(subarray([10, 5, 2, 7, 1, 9], 15))
# Output: 4




# Using two loops
# Time Complexity: O(N^2)
# Space Complexity O(1)
def subarray(arr, k):
    max_len = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum == k:
                max_len = max(max_len, j - i + 1)
    return max_len
print(subarray([10, 5, 2, 7, 1, 9], 15))
# Output: 4
print(subarray([1, -1, 5, -2, 3], 3))
# Output: 4



# Optimal Approach using Hashing
# Time Complexity: O(N) or O(NlogN)
# Space COmplexity; O(N)
def subarray(arr, k):
    n = len(arr)
    sum_map = {}
    sum = 0
    maxlen = 0
    for i in range(n):
        sum += arr[i]
        if sum == k:
            maxlen = max(maxlen, i + 1)
        rem = sum - k
        if rem in sum_map:
            length = i - sum_map[rem]
            maxlen = max(maxlen, length)
        if sum not in sum_map:
            sum_map[sum] = i
    return maxlen
print(subarray([10, 5, 2, 7, 1, 9], 15))
# Output: 4
print(subarray([1, -1, 5, -2, 3], 3))
# Output: 4



# Optimal Approach using 2pointers
# Time Complexity: O(2N)
# Space Complexity: O(1)
def subarray(arr, k):
    n = len(arr)
    left = 0
    right = 0
    maxlen = 0
    sum = arr[0]
    while right < n:
        while left <= right and sum > k:
            sum -= arr[left]
            left += 1
        if sum == k:
            maxlen = max(maxlen, right - left + 1)
        right += 1
        if right < n:
            sum += arr[right]
    return maxlen
print(subarray([10, 5, 2, 7, 1, 9], 15))
# output : 4
