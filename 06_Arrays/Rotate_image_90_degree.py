# better Approach
# Time COmplexity: O(N^2)
# Space Complexity: O(N^2)
def rotateImage(matrix,n):
    rotated = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = matrix[i][j]
    return rotated
print(rotateImage([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]], 3))
# output: [[7, 4, 1], 
        # [8, 5, 2], 
        # [9, 6, 3]]



# Optimal Solution
# Time COmplexity: O(N^2)
# Space Complexity O(1)
def rotateImage(matrix, n):
    for i in range(n):
        for j in range(i + 1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()
    return matrix
print(rotateImage([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]], 3))
# output: [[7, 4, 1], 
        # [8, 5, 2], 
        # [9, 6, 3]]