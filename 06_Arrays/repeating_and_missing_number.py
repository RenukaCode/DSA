# Brute Force Approach
# Time Complexity: O(N^2)
# Space Complexity: O(1)
def findElements(num, n):
    missing = -1
    repeating = -1
    for i in range(1, n + 1):
        count = 0
        for j in range(n):
            if num[j] == i:
                count += 1
        if count == 2:
            repeating = i
        elif count == 0:
            missing = i 
        if repeating != -1 and missing != -1:
            break
    return [repeating, missing]
print(findElements([3, 1, 2, 5, 4, 6, 7, 5], 8))
# [5, 8]
print(findElements([3,1,2,5,3], 5))
#  [3, 4]



# Better Approach
# Time Complexity: O(2N)
# Space Complexity: O(N)
def findElements(nums, n):
    missing = -1
    repeating = -1
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for num in range(1, n + 1):
        if num not in freq:
            missing = num
        elif freq[num] == 2:
            repeating = num
    return [repeating, missing]
print(findElements([3, 1, 2, 5, 4, 6, 7, 5], 8))
# [5, 8]
print(findElements([3,1,2,5,3], 5))
#  [3, 4]
        


# Optimal Approach 1
# Time Complexity: O(N)
# Space Complexity: O(1)       
def findElements(nums, n):
    sn = (n * (n + 1)) // 2
    sn2 = (n * (n + 1) * (2 * n + 1)) // 6
    s, s2 = 0, 0
    for i in range(n):
        s += nums[i]
        s2 += nums[i] * nums[i]
    val1 = s - sn
    val2 = s2 - sn2
    val2 = val2 // val1
    x = (val1 + val2) // 2
    y = x - val1
    return [x, y]
print(findElements([3, 1, 2, 5, 4, 6, 7, 5], 8))
# [5, 8]
print(findElements([3,1,2,5,3], 5))
#  [3, 4]



# Optimal Approach 2
# Time Complexity: O(N)
# Space Complexity: O(1)
def findElements(nums, n):
    xor_all = 0
    for num in nums:
        xor_all ^= num
    for i in range(1, n + 1):
        xor_all ^= i
    set_bit = xor_all & -xor_all
    x, y = 0, 0
    for num in nums:
        if num & set_bit:
            x ^= num
        else:
            y ^= num
    for i in range(1, n + 1):
        if i & set_bit:
            x ^= i
        else:
            y ^= i
    if nums.count(x) == 2:
        return [x, y]
    else:
        return [y, x]
print(findElements([3, 1, 2, 5, 4, 6, 7, 5], 8))
# [5, 8]
print(findElements([3,1,2,5,3], 5))
#  [3, 4]