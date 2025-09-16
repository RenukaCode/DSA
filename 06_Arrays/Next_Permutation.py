# Brute Force Approach
# TIme Complexity: O(N!xN)
# Space Complexity: O(1)
from itertools import permutations
def next_permutation(nums):
    perms = sorted(set(permutations(nums)))
    idx = perms.index(tuple(nums))
    if idx + 1 < len(perms):
        return perms[idx + 1]
    else:
        return perms[0]
print(next_permutation([1, 2, 3]))   #perms are: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# output: (1, 3, 2)
print(next_permutation([3, 2, 1]))
# output: (1, 2, 3)



# Better Approach
# Time Complexity: O(N)
# Space Complexity: O(1)
def next_permutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])
    return nums
print(next_permutation([1, 2, 3]))
#  output: [1, 3, 2]
print(next_permutation([3, 2, 1]))
# output: [1, 2, 3]
print(next_permutation([2, 1, 5, 4, 3, 0, 0]))