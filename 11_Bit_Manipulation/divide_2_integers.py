# Brute Force Approach
# Time Complexity: O(dividend)
# Space Complexity: O(1)
def fn(dividend,divisor):
    if dividend == divisor:
        return 1
    if dividend == -2*31 and divisor == -1:
        return 2**31-1
    if divisor == 1:
        return dividend
    isPos = True
    if dividend >= 0 and divisor < 0:
        isPos = False
    elif dividend < 0 and divisor > 0:
        isPos = False
    n = abs(dividend)
    d = abs(divisor)
    cnt = 0
    sum = 0
    while sum + d <= n:
        cnt += 1
        sum += d
    if cnt > 2**31-1 and isPos:
        return 2**31-1
    if cnt > 2**31 and not isPos:
        return -2**31
    return cnt if isPos else -cnt
print(fn(10,3)) # 3
print(fn(7,-3)) # -2
print(fn(-10,3)) # -3
print(fn(-7,-3)) # 2