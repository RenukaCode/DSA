
# Brute Force Approach
# Time complexity: O(N)
# Space complexity: O(1)
def isPrime(n):
    cnt = 0
    for i in range(1, n + 1):
        if(n % i == 0):
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False
print(isPrime(7))
print(isPrime(4))



# Optimal solution
# Time complexity: O(sqrt(N))
# Space compelxity: O(1)
import math
def isPrime(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            cnt += 1
            if n // i != i:
                cnt += 1
    if cnt == 2:
        return True
    else:
        return False
print(isPrime(7)) # true
print(isPrime(4))  # false
print(isPrime(13)) # false