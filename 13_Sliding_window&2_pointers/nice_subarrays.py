# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity:O(1)
def fn(nums,k):
    cnt=0
    for i in range(len(nums)):
        oddcnt=0
        for j in range(i,len(nums)):
            if nums[j]%2 != 0:
                oddcnt+=1
            if oddcnt>k:
                break
            if oddcnt==k:
                cnt+=1
    return cnt
print(fn([1, 1, 2, 1, 1],3)) #2
print(fn([4, 8, 2],1))       #0



# Better Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def fn(nums,k):
    freq={0:1}
    oddcnt=0
    res=0
    for num in nums:
        if num%2 != 0:
            oddcnt+=1
        res+=freq.get(oddcnt-k,0)
        freq[oddcnt]=freq.get(oddcnt,0)+1
    return res
print(fn([1, 1, 2, 1, 1],3))  #2
print(fn([4, 8, 2],1))       #0



# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def atmost(nums,k):
    left=0
    res=0
    for right in range(len(nums)):
        if nums[right] % 2 != 0:
            k-=1
        while k < 0:
            if nums[left]%2 != 0:
                k+=1
            left+=1
        res+=(right-left+1)
    return res
def fn(nums,k):
    return atmost(nums,k)-atmost(nums,k-1)
print(fn([1, 1, 2, 1, 1],3))  #2
print(fn([4, 8, 2],1))       #0

