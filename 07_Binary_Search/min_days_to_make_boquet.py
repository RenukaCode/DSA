# Brute Force Approach
# Time Complexity: O((max(arr[])-min(arr[])+1)
# Space Complexity: O(1)
def days(arr, m, k):
    n = len(arr)
    if m * k > n:
        return -1
    mini = min(arr)
    maxi = max(arr)
    for day in range(mini, maxi + 1):
        boquets = 0
        count = 0
        for i in range(n):
            if arr[i] <= day:
                count += 1
                if count == k:
                    boquets += 1
                    count = 0
            else:
                count = 0
        if boquets == m:
            return day
    return -1
print(days([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
# 12
print(days([1, 10, 3, 10, 2], 3, 2))
# -1



# Optimal Solution
# Time Complexity: O(LogN)
# Space Complexity: O(1)
def days(arr, m, k):
    n = len(arr)
    if m * k > n:
        return -1
    high = max(arr)
    low = min(arr)
    res = -1
    while low <= high:
        mid = (low + high) // 2
        count = 0
        boquets = 0
        for i in range(n):
            if arr[i] <= mid:
                count += 1
                if count == k:
                    boquets += 1
                    count = 0
            else:
                count = 0
        if boquets == m:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res
print(days([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
# 12
print(days([1, 10, 3, 10, 2], 3, 2))
# -1

        
