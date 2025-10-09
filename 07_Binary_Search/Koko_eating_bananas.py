# Brute Force Approach
# Time Complexity: O(piles[]*n)
# Space COmplexity: O(1)
import math
def fn(piles, h):
    max_speed = max(piles)
    for k in range(1, max_speed + 1):
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        if hours <= h:
            return k
    return max_speed
print(fn([7, 15, 6, 3], 8))
# 8
print(fn([25, 12, 8, 14, 19], 5))
# 25



# Optimal Solution
# Time Complexity: O(LogN)
# Space Complexity: O(1)
def fn(piles, h):
    maxi = float('-inf')
    low = 1
    high = max(piles)
    res = high
    while low <= high:
        mid = (low + high) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p / mid)
        if hours <= h:
            res =  mid
            high = mid - 1
        else:
            low = mid + 1
    return res
print(fn([7, 15, 6, 3], 8))
# 8
print(fn([25, 12, 8, 14, 19], 5))
# 25
