# Brute Force Approach
# Time Complexity: O(N*M)
# Space Complexity: O(1)
def fn(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == target:
                return True
    return False
print(fn([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
# True
print(fn([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))
# False



# Better Approach
# Time Complexity: O(N * LogM)
# Space Complexity: O(1)
def fn(matrix,target):
    n = len(matrix)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if matrix[mid] == target:
            return True
        elif target > matrix[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False
def search(matrix,target):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        if matrix[i][0] <= target <= matrix[i][m - 1]:
            return fn(matrix[i],target)
    return False
print(search([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
# True
print(search([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))
# False



# Optimal Solution
# Time Complexity: O(log(N*M))
# Space Complexity: O(1)
def fn(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        row = mid // m
        col = mid % m
        if matrix[row][col] == target:
            return True
        elif target > matrix[row][col]:
            low = mid + 1
        else:
            high = mid - 1
    return False
print(fn([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
# True
print(fn([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))
# False
