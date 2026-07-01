# Brute Force Approach
# Time Complexity: O(logn) due int to binary conversion
# Space Complexity: O(logn) - for binary str
def fn(n,i):
    binary = bin(n)[2:]
    if i >= len(binary):
        return False
    return binary[-(i+1)] == '1'
print(fn(5,0)) # True
print(fn(10,1)) # True
print(fn(10,2)) # False



# Optimal Approach
# Time Complexity: O(1)
# Space Complexity: O(1)
def fn(n,i):
    return (n & (1 << i)) != 0
print(fn(5,0)) # True
print(fn(10,1)) # True
print(fn(10,2)) # False
