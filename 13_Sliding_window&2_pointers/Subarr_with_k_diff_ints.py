# Brute Force Approach
# Time Complexity: O(N²*K)
# Space Complexity: O(k)
def fn(nums,k):
    cnt=0
    for i in range(len(nums)):
        freq={}
        for j in range(i,len(nums)):
            freq[nums[j]] = freq.get(nums[j],0)+1
            if len(freq) == k:
                cnt+=1
            if len(freq)>k:
                break
    return cnt
print(fn([1,2,1,2,3],2))  # 7
print(fn([1,2,1,3,4],3))  # 3



# Optimal Solution
# Time Complexity: O(n)
# Space Complexity: O(k)
def atmost(nums,k):
    freq={}
    l=0
    cnt=0
    for r in range(len(nums)):
        if nums[r] not in freq or freq[nums[r]] == 0:
            k-=1
        freq[nums[r]] = freq.get(nums[r],0)+1
        while k<0:
            freq[nums[l]] -= 1
            if freq[nums[l]] == 0:
                k+=1
            l+=1
        cnt+=(r-l+1)
    return cnt
def subarray(nums,k):
    return atmost(nums,k)-atmost(nums,k-1)
print(subarray([1,2,1,2,3],2))  # 7
print(subarray([1,2,1,3,4],3))  # 3



# Optimal Solution
# Time Complexity: O(n)
# Space Complexity: O(k)
def fn(nums,k):
    if k==0 or not nums:
        return 0
    maxlen=0
    l=0
    freq={}
    for r in range(l,len(nums)):
        freq[nums[r]] = freq.get(nums[r],0)+1
        while len(freq)>k:
            freq[nums[l]] -= 1
            if freq[nums[l]] == 0:
                del freq[nums[l]]
            l+=1
        maxlen=max(maxlen,r-l+1)
    return maxlen
print(subarray([1,2,1,2,3],2))  # 7
print(subarray([1,2,1,3,4],3))  # 3