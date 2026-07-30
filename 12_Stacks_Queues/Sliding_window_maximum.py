# Brute Force Approach
# Time Complexity: O(n * k)
# Space Complexity: O(1)
def fn(nums,k):
    res=[]
    for i in range(len(nums)-k+1):
        window=nums[i:i+k]
        res.append(max(window))
    return res
print(fn([4, 0, -1, 3, 5, 3, 6, 8],3))  # [4, 3, 5, 5, 6, 8]



# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
from collections import deque
def fn(nums,k):
    dq=deque()
    res=[]
    for i in range(len(nums)):
        if dq and dq[0]<=i-k:
            dq.popleft()
        if dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i>=k-1:
            res.append(nums[dq[0]])
    return res
print(fn([4, 0, -1, 3, 5, 3, 6, 8],3))  # [4, 3, 5, 5, 6, 8]