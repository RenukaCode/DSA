# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def fn(nums):
    n=len(nums)
    maxLen=0
    for i in range(n):
        hash={}
        for j in range(i,n):
            if nums[j] in hash:
                break
            hash[nums[j]]=1
            Len = j-i+1
            maxLen=max(maxLen,Len)
    return maxLen
print(fn("abcddabcbb")) #4
print(fn("cadbzabcd"))  #5



# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def fn(nums):
    n = len(nums)
    hash_map = {}  
    l, r, maxlen = 0, 0, 0
    while r < n:
        if nums[r] in hash_map and hash_map[nums[r]] >= l:
            l = hash_map[nums[r]] + 1
        maxlen = max(maxlen, r - l + 1)
        hash_map[nums[r]] = r
        r += 1
    return maxlen
print(fn("abcddabcbb")) #4
print(fn("cadbzabcd"))  #5