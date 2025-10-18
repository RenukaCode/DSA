# Brute Force Approach
# Time Complexity: O(N * (sum(arr[])-max(arr[])+1))
# Space Complexity: O(1)
def countPainters(boards, time):
    n = len(boards)
    painters = 1
    boardsPainter = 0
    for i in range(n):
        if boardsPainter + boards[i] <= time:
            boardsPainter += boards[i]
        else:
            painters += 1
            boardsPainter = boards[i]
    return painters
def fn(boards, k):
    low = max(boards)
    high = sum(boards)
    for time in range(low + high + 1):
        if countPainters(boards, time) <= k:
            return time
    return low
print(fn([5, 5, 5, 5],2))
# 10
print(fn([10, 20, 30, 40],2))
# 60



# Optimal Solution
# Time Complexity: O(N * log(sum(arr[])-max(arr[])+1))
# Space Complexity: O(1)
def countPainters(boards, time):
    n = len(boards)
    painters = 1
    boardsPainter = 0
    for i in range(n):
        if boardsPainter + boards[i] <= time:
            boardsPainter += boards[i]
        else:
            painters += 1
            boardsPainter = boards[i]
    return painters
def fn(boards,k):
    low = max(boards)
    high = sum(boards)
    res = low
    while low <= high:
        mid = (low + high) // 2
        if countPainters(boards, mid) <= k:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res
print(fn([5, 5, 5, 5],2))
# 10
print(fn([10, 20, 30, 40],2))
# 60
        
