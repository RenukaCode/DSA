# Brute Force Approach
# Time Complexity: O(m*n)
# Space Complexity: O(1)
def findMax(mat,m,n):
    count = 0
    index = -1
    for i in range(m):
        cntOnes = sum(mat[i])
        if cntOnes > count:
            count = cntOnes
            index = i
    return index
print(findMax([[1, 1, 1], [0, 0, 1], [0, 0, 0]],3,3))
# 0
print(findMax([[0,0],[0,0]],2,2))
# -1


# Optimal Solution
# Time COmplexity: O(n X logn)
# Space Complexity: O(1)
def lowerBound(arr,m,x):
    low = 0 
    high = m - 1
    ans = m
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
             low = mid + 1
    return ans
def findMax(mat,m,n):
    count = 0
    index = -1
    for i in range(m):
        cntOnes = m - lowerBound(mat[i],m,1)
        if cntOnes > count:
            count = cntOnes
            index = i
    return index
print(findMax([[1, 1, 1], [0, 0, 1], [0, 0, 0]],3,3))
# 0
print(findMax([[0,0],[0,0]],2,2))
# -1

