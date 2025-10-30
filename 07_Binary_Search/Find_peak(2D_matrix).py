# Time Complexity:  O(N * logM)
# Space Complexity: O(1)
def ele(matrix,col):
    n = len(matrix)
    peak = float('-inf')
    idx = -1
    for i in range(n):
        if matrix[i][col] > peak:
            peak = matrix[i][col]
            idx = i
    return idx
def findPeak(matrix):
    n = len(matrix)
    m = len(matrix[0])
    low = 0
    high = m - 1
    while low <= high:
        mid = (low + high) // 2
        row = ele(matrix,mid)
        left = matrix[row][mid - 1] if mid - 1 >= 0 else float('-inf')
        right = matrix[row][mid + 1] if mid + 1 < m else float('-inf')
        if matrix[row][mid] > left and matrix[row][mid] > right:
            return [row,mid]
        elif matrix[row][mid] < left:
            high = mid - 1
        else:
            low = mid + 1
    return [-1,-1]
print(findPeak([[1,2,3],[5,6,7],[9,10,11]]))
# [2, 2]
print(findPeak([[1, 2, 3], [6, 5, 4], [7, 8, 9]]))
# [2, 2]
print(findPeak([[5, 10, 8], [4, 25, 7], [3, 9, 6]]))
# [3, 3]