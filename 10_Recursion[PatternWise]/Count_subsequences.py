# Time Complexity: O(2^n)
# Space Complexity: O(n)
def fn(idx,sum,nums):
    if sum == 0:
        return 1
    if sum < 0 or idx == len(nums):
        return 0
    return fn(idx+1,sum-nums[idx],nums) + fn(idx+1,sum,nums)
def cntSubsequences(nums,target):
    return fn(0,target,nums)
print(cntSubsequences([1,3,2],3))  # 2
print(cntSubsequences([4,9,2,5,1],10))  # 2
print(cntSubsequences([4,2,10,5,1,3],5))  # 3
