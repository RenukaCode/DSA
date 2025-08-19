# Brute Force Approach
# Time complexity: O(N)
# Space complexity: O(N)
def allDivisors(n):
    res = []
    for i in range(1, n + 1):
        if n % i == 0:
           res.append(i)
    return res
print(allDivisors(36)) # [1, 2, 3, 4, 6, 9, 12, 18, 36]
print(allDivisors(2)) # [1, 2]
print(allDivisors(400)) # [1, 2, 4, 5, 8, 10, 16, 20, 25, 40, 50, 80, 100, 200, 400]
        

# Optimal Solution
# Time complexity: O(sqrt(N))
# Space complexity: O(2*sqrt(N))
import math
def allDivisors(n):
    res = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n // i)
    return res 
print(allDivisors(36))  # [1, 36, 2, 18, 3, 12, 4, 9, 6]   
print(allDivisors(2))   # [1, 2]
