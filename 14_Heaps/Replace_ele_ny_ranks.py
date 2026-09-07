# Brute Force Approach:
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def fn(nums):
    res=[]
    for i in range(len(nums)):
        smaller=set()
        for j in range(len(nums)):
            if nums[j]<nums[i]:
                smaller.add(nums[j])
        rank=len(smaller)+1
        res.append(rank)
    return res
print(fn([40,10,20,30]))  # [4,1,2,3]
print(fn([100,100,100]))  # [1,1,1]
print(fn([37,12,28,9,100,56,80,5,12]))  # [5,3,4,2,8,6,7,1,3]



# Optimal Solution:
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
def fn(nums):
    sortedArr = sorted(nums)
    mp={}
    rank=1
    for num in sortedArr:
        if num not in mp:
            mp[num]=rank
            rank+=1
    res=[mp[num] for num in nums]
    return res
print(fn([40,10,20,30]))  # [4,1,2,3]
print(fn([100,100,100]))  # [1,1,1]
print(fn([37,12,28,9,100,56,80,5,12]))  # [5,3,4,2,8,6,7,1,3]