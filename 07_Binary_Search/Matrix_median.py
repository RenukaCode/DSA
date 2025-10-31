# Brute Force Approach
# Time Complexity: O(N*M*log(N*M))
# Space Complexity: O(N*M)
def median(mat):
    arr = []
    for i in mat:
        for j in i:
            arr.append(j)
    arr.sort()
    return arr[len(arr) // 2]
print(median([[1,3,5],[2,6,9],[3,6,9]]))
# 5 
print(median([[1,2,3],[7,8,9],[3,4,5]]))
# 4



# Optimal Approach
# Time Complexity: O(N * logM)
# Space Complexity: O(1)
def cnt(row,mid):
    low = 0
    high = len(row) - 1
    while low <= high:
        idx = (low + high) // 2
        if row[idx] <= mid:
            low = idx + 1
        else:
            high = idx - 1
    return low
def median(mat):
    row = len(mat)
    col = len(mat[0])
    low = min(row[0] for row in mat)
    high = max(row[-1] for row in mat)
    while low <= high:
        mid = (low + high) // 2
        count = 0
        for i in mat:
            count += cnt(i,mid)
        if count < (row * col + 1) // 2:
            low = mid + 1
        else:
            high = mid - 1
    return low
print(median([[1,3,5],[2,6,9],[3,6,9]]))
# 5
print(median([[1,2,3],[7,8,9],[3,4,5]]))
# 4