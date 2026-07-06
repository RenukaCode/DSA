# Brute Force Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def fn(x,n):
    if n == 0: 
        return 1
    if n == 1.0:
        return x
    temp = n
    if n < 0:
        x = 1/x
        temp = -1*n
    ans = 1
    for i in range(temp):
        ans *= x
    return ans
print(fn(2.0000,10)) #1024.0
print(fn(2.0000,-2)) #0.25
print(fn(2.00,1)) #2.00



# Optimal Solution
# Time Complexity: O(logn)
# Space Complexity: O(logn)
def pow(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n%2 == 0:
        return pow(x*x,n//2)
    return x*pow(x,n-1)
def fn(x,n):
    if n < 0:
        return 1.0/pow(x,-n)
    return pow(x,n)
print(fn(2.0000,10)) #1024.0
print(fn(2.0000,-2)) #0.25
print(fn(2.00,1)) #2.00