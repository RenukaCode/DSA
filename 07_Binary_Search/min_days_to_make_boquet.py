# Brute Force Approach
# Time Complexity: O((max(arr[])-min(arr[])+1)
# Space Complexity: O(1)
def pos(arr, day, m, k):
    n = len(arr)
    noOfB = 0
    count= 0
    for i in range(n):
        if arr[i] <= day:
            count += 1
        else:
            noOfB += count // k
            count = 0
    noOfB += count // k
    return noOfB >= m
def fn(arr, k, m):
    n = len(arr)
    val = m * k
    if val > n:
        return -1
    mini = float('inf')
    maxi = float('-inf')
    for i in range(n):
        mini = min(mini, arr[i])
        maxi = max(maxi, arr[i])
    for i in range(mini, maxi + 1):
        if pos(arr, i, m, k):
            return i
    return -1
print(fn([7, 7, 7, 7, 13, 11, 12, 7], 3, 2))
# 12
