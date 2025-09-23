# Brute Force Approach(three loops)
# Time Complexity: O(N^3)
# Space Complexity: O(1)
def subarraysWithXorK(nums, k) -> int:
    n = len(nums)
    count = 0
    for i in range(0, n):
        for j in range(i, n):
            xorr = 0
            for l in range(i, j + 1):
                xorr = xorr ^ nums[l]
            if (xorr == k):
                count += 1
    return count 
print(subarraysWithXorK([4, 2, 2, 6, 4], 6))
#  4
print(subarraysWithXorK([5, 6, 7, 8, 9], 5))
#  2



# Better Approach(two loops)
# Time Complexity: O(N^2)
# Space Complexity: O(1)
def subarrayWithXorK(nums, k):
    n = len(nums)
    xorr = 0
    count = 0
    for i in range(n):
        for j in range(i, n):
            xorr = xorr ^ nums[j]
            if xorr == k:
                count += 1
    return xorr
print(subarraysWithXorK([4, 2, 2, 6, 4], 6))
#  4
print(subarraysWithXorK([5, 6, 7, 8, 9], 5))
#  2



# Optimal Approach(Hashing)
# Time Complexity: O(N)
# Space Complexity: O(N)
def subaarayWithXorK(nums, k):
    n = len(nums)
    xorr = 0
    freq = {}
    freq[xorr] = 1
    count = 0
    for i in range(n):
        xorr = xorr ^ nums[i]
        x = xorr ^ k
        count += freq[x]
        freq[xorr] += 1
    return count
print(subarraysWithXorK([4, 2, 2, 6, 4], 6))
#  4
print(subarraysWithXorK([5, 6, 7, 8, 9], 5))
#  2