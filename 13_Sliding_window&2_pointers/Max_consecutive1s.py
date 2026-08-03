# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def fn(nums,k):
    maxlen=0
    for i in range(len(nums)):
        zeroes=0
        for j in range(i, len(nums)):
            if nums[j]==0:
                zeroes += 1
            if zeroes > k:
                break
            maxlen = max(maxlen,j-i+1)
    return maxlen
print(fn([1,1,0,0,1,1,1,0,1],2)) #7
print(fn([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],3)) #10



# Better Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def fn(nums,k):
    windsize=0
    l=0
    zeroes=0
    for r in range(len(nums)):
        if nums[r]==0:
            zeroes+=1
        while zeroes>k:
            if nums[l]==0:
                zeroes -= 1
            l += 1
        windsize = max(windsize,r-l+1)
    return windsize
print(fn([1,1,0,0,1,1,1,0,1],2)) #7
print(fn([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],3)) #10



# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def fn(nums,k):
    windsize = 0
    l = 0
    zeroes = 0
    for r in range(len(nums)):
        if nums[r]==0:
            zeroes+=1
        if zeroes>k:
            if nums[l]==0:
                zeroes -= 1
            l += 1
        windsize = max(windsize,r-l+1)
    return windsize
print(fn([1,1,0,0,1,1,1,0,1],2)) #7
print(fn([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],3)) #10