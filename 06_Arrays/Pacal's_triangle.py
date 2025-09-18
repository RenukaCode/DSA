# Variation-1 (element at position)
# Time Complexity: O(N)
# Space Complexity: O(1)
def pascalsTriangle(r, c):
    def fact(x):
        if x == 0 or x == 1:
            return 1
        return x * fact(x - 1)
    formula = fact(r - 1) // (fact(c - 1) * fact(r - c ))
    return formula
print(pascalsTriangle(5, 3))
#  output : 6


# Variation-2(nth row)
# Time Complexity: O(r)
# Space Complexity: O(r)
def pascalsTriangle(r):
    n = r 
    val = 1
    row = []
    for i in range(1, n + 1):
        row.append(val)
        val = val * (n - i)
        val = val  // i
    return row
print(pascalsTriangle(5))
#  [1, 4, 6, 4, 1]
    

def pascalsTriangle(n):
    triangle = []
    for row in range(0, n):
        currentRow = []
        for col in range(0, row + 1):
            
            if col == 0 or col == row:
                currentRow.append(1)
            else:
                value = triangle[row - 1][col - 1] + triangle[row - 1][col]
                currentRow.append(value)
        triangle.append(currentRow)
    return triangle
print(pascalsTriangle(5))
#  [[1],
#  [1, 1],
#  [1, 2, 1],
#  [1, 3, 3, 1],
#  [1, 4, 6, 4, 1]]


