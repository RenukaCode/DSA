# Brute Force Approach
# Time Complexity: O(N2)
# Space Complexity: O(1)
def missingNumbers(arr, N):
    for i in range(1, N + 1):
        flag = 0
        for j in range(len(arr)):
            if arr[j] == i:
                flag = 1
                break
        if flag == 0:
            return i
    return -1
# Example usage:
print(missingNumbers([1, 2, 3, 5], 5))  
# Output: 4
print(missingNumbers([1, 3], 3))
# Output: 2
print(missingNumbers([2, 2, 3, 4,], 4))
# Output: 1



# Better Approach using Hashing
# Time Complexity: O(N)
# Space Complexity: O(N)
def missingNumbers(arr, N):
    hash = [0] * (N + 1)
    for i in range(N - 1):
        hash[arr[i]] += 1
    for i in range(1, N + 1):
        if hash[i] == 0:
            return i
    return -1
# Example usage:
print(missingNumbers([1, 2, 3, 5], 5))
# output: 4
print(missingNumbers([1, 3,], 3))
# Output: 2



# Optimal Approach using sum formula
# Time Complexity: O(N)
# Space Complexity: O(1)
def missingNumbers(arr, n):
    sum_n = (n *(n + 1)) // 2
    sum_arr = sum(arr)
    missing = sum_n - sum_arr
    return missing
# Example usage:
print(missingNumbers([1, 2, 3, 5], 5))
# Output: 4
print(missingNumbers([1, 3], 3))
# Output: 2



# Optimal Approach using XOR
# Time Complexity: O(N)
# Space Complexity: O(1)
def missingNumbers(arr, N):
    XOR1= 0
    XOR2 = 0
    for i in range(N - 1):
        XOR1 = XOR1 ^ arr[i]
        XOR2 = XOR2 ^ (i + 1)
    XOR2 = XOR2 ^ N
    missing = XOR1 ^ XOR2
    return missing
print(missingNumbers([1, 2, 3, 5], 5))
# Output: 4
print(missingNumbers([1, 3], 3))
# Output: 2