# Brute Force Approach
# Time complexity: O((N*M)*(N + M)) + O(N*M)
# Space Complexity: O(1)
def zeroMatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                for k in range(m):
                    if matrix[i][k] != 0:
                        matrix[i][k] = -1
                for k in range(n):
                    if matrix[k][j] != 0:
                        matrix[k][j] = -1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    return matrix
matrix = [[1, 1, 1],
          [1, 0, 1],
          [1, 1, 1]]
print(zeroMatrix(matrix))
#  output: [[1, 0, 1],
          # [0, 0, 0],
          # [1, 0, 1]]


def zero_matrix(matrix):
    if not matrix or not matrix[0]:
        return matrix
    n, m = len(matrix), len(matrix[0])
    col0 = 0
    for i in range(n):
        if matrix[i][0] == 0:
            col0 = 0
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0
    return matrix
matrix = [[1, 1, 1],
          [1, 0, 1],
          [1, 1, 1]]
print(zero_matrix(matrix))
#  output: [[1, 0, 1],
          # [0, 0, 0],
          # [1, 0, 1]]           
