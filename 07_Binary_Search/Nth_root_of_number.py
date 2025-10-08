# Brute Force Approach
# Time Complexity: O(N*LogN)
# Space Complexity: O(1)
def fn(b, exp):
    ans = 1
    base = b
    while exp > 0:
        if exp % 2:
            exp -= 1
            ans = ans * base
        else:
            exp //= 2
            base = base * base
    return ans
print(fn(3, 3))
# 27
print(fn(3, 4))
# 81



# Optimal Solution
# Time Complexity: O(LogN)
# Space Complexity: O(1)
def fn(mid, n, m):
    ans = 1
    for i in range(1, n + 1):
        ans *= mid
        if ans > m:
            return 2
    if ans == m:
        return 1
    return 0
def nthRoot(n, m):
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        midN = fn(mid, n, m)
        if midN == 1:
            return mid
        elif midN == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1
print(nthRoot(3, 27))
# 3
print(nthRoot(4, 69))
#  -1