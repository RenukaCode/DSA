# Brute Force Approach
# Time Complexity:  O(NlogN) + O(N *(max(stalls[])-min(stalls[])))
# Space Complexity: (1)
def fn(stalls, dist, cows):
    n = len(stalls)
    last = stalls[0]
    count = 1
    for i in range(1, n):
        if stalls[i] - last >= dist:
            count += 1
            last = stalls[i]
        if count >= cows:
            return True
    return False
def aggressiveCows(stalls, k):
    n = len(stalls)
    stalls.sort()
    maxLimit = stalls[n-1] - stalls[0]
    for i in range(1, maxLimit + 1):
        if not fn(stalls, i, k):
            return i - 1
    return maxLimit
print(aggressiveCows([0, 3, 4, 7, 10, 9],4))
# 3
print(aggressiveCows([4,2,1,3,6],2))
# 5



# Optimal Solution
# Time Complexity:  O(NlogN) + O(N * log(max(stalls[])-min(stalls[])))
# Space Complexity: O(1)
def fn(stalls, dist, cows):
    n = len(stalls)
    count = 1
    last = stalls[0]
    for i in range(1, n):
        if stalls[i] - last >= dist:
            count += 1
            last = stalls[i]
        if count >= cows:
            return True
    return False
def aggressiveCows(stalls, k):
    n = len(stalls)
    stalls.sort()
    low = 1
    high = stalls[n-1] - stalls[0]
    while low <= high:
        mid = (low + high) // 2
        if fn(stalls, mid, k):
            low = mid + 1
        else:
            high = mid - 1
    return high
print(aggressiveCows([0, 3, 4, 7, 10, 9],4))
# 3
print(aggressiveCows([4,2,1,3,6],2))
# 5