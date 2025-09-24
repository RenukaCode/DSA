# Brute Force Approach
# Time Complexity: O(O(N*logN) + O(2*N))
# Space Complexity: O(N)
def mergeIntervals(arr: list[list[int]]) -> list[list[int]]:
    arr.sort()
    ans = []
    for i in range(len(arr)):
        start = arr[i][0]
        end = arr[i][1]
        if ans and end <= ans[-1][1]:
            continue
        for j in range(i + 1, len(arr)):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])
            else:
                break
        ans.append([start, end])
    return ans
print(mergeIntervals([[1, 3], [8, 10], [2, 6], [15, 18]]))
#  [[1, 6], [8, 10], [15, 18]]
print(mergeIntervals( [[1,4],[4,5]]))
#  [[1, 5]]



# Optimal Solution
# Time Complexity: O(O(N*logN) + O(N))
# Space Complexity: O(N)
def mergeIntervals(arr:list[list[int]]) -> list[list[int]]:
    n = len(arr)
    arr.sort()
    ans = []
    for i in range(n):
        if not ans or arr[i][0] > ans[-1][1]:
            ans.append(arr[i])
        else:
            ans[-1][1] = max(ans[-1][1], arr[i][1])
    return ans
print(mergeIntervals([[1, 3], [8, 10], [2, 6], [15, 18]]))
#  [[1, 6], [8, 10], [15, 18]]
print(mergeIntervals( [[1,4],[4,5]]))
#  [[1, 5]]
