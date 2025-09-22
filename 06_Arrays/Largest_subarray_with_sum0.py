# Brute Force Approach
# Time Complexity: O(N^2)
# Space Complexity: O(1)
def subarray(nums, n):
    maxlen = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if sum == 0:
                maxlen = max(maxlen, j - i + 1)
    return maxlen
print(subarray([9, -3, 3, -1, 6, -5], 6))
# 5
print(subarray([6, -2, 2, -8, 1, 7, 4, -10], 8))
#  8



# Optimal Approach
# Time Complexity: O(N)
# Space Complexity: O(N)
def subarray(nums, n):
    freq = {}
    maxlen = 0
    sum = 0
    for i in range(n):
        sum += nums[i]
        if sum == 0:
            maxlen = i + 1
        else:
            if sum in freq:
                maxlen = max(maxlen, i - freq[sum])
            else:
                freq[sum] = i
    return maxlen
print(subarray([6, -2, 2, -8, 1, 7, 4, -10], 8))
#  8
print(subarray([9, -3, 3, -1, 6, -5], 6))
#  5





            



        
