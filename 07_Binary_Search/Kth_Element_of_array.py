# Brute Force Approach
# Time Complexity: O(m + n)
# Space Complexity: O(m + n)
def fn(a,b,m,n,k):
    nums = []
    i = j = 0
    while i < m and j < n:
        if a[i] < b[j]:
            nums.append(a[i])
            i += 1
        else:
            nums.append(b[j])
            j += 1
    nums.extend(a[i:])
    nums.extend(b[j:])
    return nums[k - 1]
print(fn([2, 3, 6, 7, 9],[1, 4, 8, 10],5,4,5))
# 6



# Better Approach
# Time Complexity: O(m + n)
# Space Complexity: O(1)
def fn(a,b,m,n,k):
    i = j = 0
    cnt = 0
    res = -1
    while i < m and j < n:
        if a[i] < b[j]:
            if cnt == k - 1:
                res = a[i]
            cnt += 1
            i += 1
        else:
            if cnt == k - 1:
                res = b[j]
            cnt += 1
            j += 1
    while i < m:
        if cnt == k - 1:
            res = a[i]
        cnt += 1
        i += 1
    while j < n:
        if cnt == k - 1:
            res = b[j]
        cnt += 1
        j += 1
    return res
print(fn([2, 3, 6, 7, 9],[1, 4, 8, 10],5,4,5))
# 6



# Optimal Solution
# Time Complexity: O(log(min(m, n)))
# Space Complexity: O(1)
def fn(a,b,m,n,k):
    if m > n:
        return fn(a,b,n,m,k)
    left = k
    low = max(0,k - n)
    high = min(k, m)
    while low <= high:
        mid1 = (low + high ) // 2
        mid2 = left - mid1
        i1 = float('-inf')
        i2 = float('-inf')
        r1 = float('inf')
        r2 = float('inf')
        if mid1< m:
            r1 = a[mid1]
        if mid2 < n:
            r2 = b[mid2]
        if mid1 - 1 >= 0:
            i1 = a[mid1 - 1]
        if mid2 - 1 >= 0:
            i2 = b[mid2 - 1]
        if i1 <= r2 and i2 <= r1:
            return max(i1, i2)
        elif i1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    return 0
print(fn([2, 3, 6, 7, 9],[1, 4, 8, 10],5,4,5))
# 6