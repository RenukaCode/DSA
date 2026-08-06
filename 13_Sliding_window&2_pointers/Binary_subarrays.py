# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def fn(nums,goal):
    cnt=0
    for i in range(len(nums)):
        total=0
        for j in range(i,len(nums)):
            total += nums[j]
            if total == goal:
                cnt+=1
    return cnt
print(fn([1,0,1,0,1],2)) #4
print(fn([1, 0, 0, 1, 1, 0],2))  #7



# Better Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def fn(nums,goal):
    prefixsum={0:1}
    cnt=0
    currsum=0
    for num in nums:
        currsum+=num
        if currsum-goal in prefixsum:
            cnt+=prefixsum[currsum-goal]
        prefixsum[currsum] = prefixsum.get(currsum,0)+1
    return cnt
print(fn([1,0,1,0,1],2)) #4
print(fn([1, 0, 0, 1, 1, 0],2))  #7



# Optimal Approach
# Time Complexity: O(n)
# Space Complexity:O(1)
def fn(nums,goal):
    return atmost(nums,goal)-atmost(nums,goal-1)
def atmost(nums,k):
    if k<0:
        return 0
    left=0
    total=0
    currsum=0
    for right in range(len(nums)):
        currsum+=nums[right]
        while currsum>k:
            currsum-=nums[left]
            left+=1
        total+=(right-left+1)
    return total
print(fn([1,0,1,0,1],2)) #4
print(fn([1, 0, 0, 1, 1, 0],2))  #7
