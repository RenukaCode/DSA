# Brute Force Approach
# Time Complexity: O(N)
# Space Complexity: O(N)
def fn(n):
    res = []
    for i in range(1, n+1):
        if n % i == 0:
            res.append(i)
    return res
print(fn(36))  #[1, 2, 3, 4, 6, 9, 12, 18, 36]
print(fn(144)) #[1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 36, 48, 72, 144]



# Optimal Approach
# Time Complexity: O(sqrt(n))
# Space Complexity: O(2*sqrt(n))
import math
def fn(n):
    res = []
    for i in range(1, math.isqrt(n)+1):
        if n%i == 0:
            res.append(i)
            if i != n//i:
                res.append(n//i)
    return res
print(fn(36))  #[1, 2, 3, 4, 6, 9, 12, 18, 36]
print(fn(144)) #[1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 36, 48, 72, 144]