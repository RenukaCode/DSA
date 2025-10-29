# Brute Force Approach
# Time Complexity: O(N*M)
# Space Complexity: O(1)
def fn(matrix,target):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == target:
                return True
    return False
print(fn([[1,3,5,7],[10,11,16,20],[23,30,34,60]],60))
# True
print(fn([[1,3,5,7],[10,11,16,20],[23,30,34,60]],2))
# False



# Better Approach
# Time Complexity: O(N * LogM)
# Space Complexity: O(1)
def fn(matrix,target):
    low = 0
    high = len(matrix) - 1
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
        check = fn(matrix[i], target)
        if check:
            return True
    return False
print(search([[1,3,5,7],[10,11,16,20],[23,30,34,60]],60))
# True
print(search([[1,3,5,7],[10,11,16,20],[23,30,34,60]],2))
# False



# Optimal Solution
# Time Complexity: O(N + M)
# Space Complexity: O(1)
def search(matrix,target):
    n = len(matrix)
    m = len(matrix[0])
    row = 0
    col = m - 1
    while row < n and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False
print(search([[1,3,5,7],[10,11,16,20],[23,30,34,60]],60))
# True
print(search([[1,3,5,7],[10,11,16,20],[23,30,34,60]],2))
# False
