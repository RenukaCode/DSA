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
print(subarray([1, -1, 5, -2, 3], 3))
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