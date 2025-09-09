# Brute Force Approach
# Time Compplexity: O(N^2)
# Space Complexity: O(N)
def leaders(arr, n):
    ans = []
    for i in range(n):
        leader = True
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                leader = False
                break
        if leader:
            ans.append(arr[i])
    return ans
print(leaders([ 10, 22, 12, 3, 0, 6], 6))
#  [22, 12, 6]
print(leaders([4, 7, 1, 0], 4))
#  [7, 1, 0]



# Optimal Solution
# Time Complexity: O(N)
# Space Complexity: O(N)
def leaders(arr, n):
    ans = []
    maxLeader = arr[n - 1]
    ans.append(arr[n - 1])  
    for i in range(n - 2, -1, -1):
        if arr[i]  > maxLeader:   
            ans.append(arr[i])
            maxLeader = arr[i]  
    ans.reverse()
    return ans
print(leaders([ 10, 22, 12, 3, 0, 6], 6))
#  [22, 12, 6]
print(leaders([4, 7, 1, 0], 4))
#  [7, 1, 0]         