# Brute Force Approach
# Time Complexity: O(2*N)
# Space Complexity: O (N)
def moveZeroes(a, n):
    temp = []
    for i in range(n):
        if a[i] != 0:
            temp.append(a[i])
    nz = len(temp)
    for i in range(nz):
        a[i] = temp[i]
    for i in range(nz, n):
        a[i] = 0
    return a
print(moveZeroes([0,1,0,3,12], 5))
# [1, 3, 12, 0, 0]
print(moveZeroes([1, 0, 2, 3, 2, 0, 0, 4, 5, 1], 10))
#  [1, 2, 3, 2, 4, 5, 1, 0, 0, 0]



# Optimal Solution
# Time Complexity: O(N)
# Space Complexity: O(1)
def moveZeroes(a, n):
    j = -1
    for i in range(n):
        if a[i] == 0:
            j = i
            break
    if j == -1:
        return a
    for i in range(j + 1, n):
        if a[i] != 0:
            a[i], a[j] = a[j], a[i]
            j += 1
    return a
print(moveZeroes([0,1,0,3,12], 5))
# [1, 3, 12, 0, 0]
print(moveZeroes([1, 0, 2, 3, 2, 0, 0, 4, 5, 1], 10))
#  [1, 2, 3, 2, 4, 5, 1, 0, 0, 0]



# Time COmplexity: O(N)
# Space Complexity: O(1)
def moveZeroes(nums):
    n = len(nums)
    j = 0
    for i in range(n):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j] , nums[i]
            j += 1
    return nums
print(moveZeroes([0,1,0,3,12]))
# [1, 3, 12, 0, 0]
print(moveZeroes([1, 0, 2, 3, 2, 0, 0, 4, 5, 1]))
#  [1, 2, 3, 2, 4, 5, 1, 0, 0, 0]
print(moveZeroes([2,1]))
# [2, 1]
print(moveZeroes([0]))
# [0]
