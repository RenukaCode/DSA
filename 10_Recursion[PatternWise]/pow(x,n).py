# Brute Force Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def myPow(x,n):
    if n == 0 or x == 1.0:
        return 1
    temp = n
    if n < 0:
        x = 1/x
        temp = -1*n
    ans = 1
    for i in range(temp):
        ans *= x
    return ans
print(myPow(2.0000, 10))               #1024.0
print(myPow(2.0000, -2))               #0.25



# Optimal Approach
# Time Complexity: O(logn)
# Space Complexity: O(logn)
def myPow(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n % 2 == 0:
        return myPow(x*x,n//2)
    return x * myPow(x,n-1)
def power(x,n):
    if n < 0:
        return 1.0/myPow(x,-n)
    return myPow(x,n)
print(power(2.0000, 10))               #1024.0
print(power(2.0000, -2))               #0.25
