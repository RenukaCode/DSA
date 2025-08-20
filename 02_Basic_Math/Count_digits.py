# Brute Force Approch
def countin(n):
    cnt = int(len(str(n)))
    return cnt
print(countin(12234345)) #8

# Optimal solution
import math
def countNum(n):
    n = abs(n)
    if n == 0:
        return 1
    cnt =  int(math.log10(n)) + 1
    return cnt

# Example usage
print(countNum(12345))  # 5
print(countNum(-9876)) # 4
print(countNum(0)) # 1
print(countNum(1000000)) # 7

