# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def fn(nums):
    maxfruits=0
    for i in range(len(nums)):
        basket={}
        curr=0
        for j in range(i,len(nums)):
            basket[nums[j]] = basket.get(nums[j],0)+1
            if len(basket)>2:
                break
            curr+=1
        maxfruits=max(maxfruits,curr)
    return maxfruits
print(fn([1,2,1])) #3
print(fn([1,2,3,2,2])) #4



# Better Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def fn(nums):
    l=0
    maxfruits=0
    basket={}
    for r in range(len(nums)):
        basket[nums[r]]=basket.get(nums[r],0)+1
        while len(basket)>2:
            basket[nums[l]]-=1
            if basket[nums[l]]==0:
                del basket[nums[l]]
            l+=1
        maxfruits=max(maxfruits,r-l+1)
    return maxfruits
print(fn([1,2,1])) #3
print(fn([1,2,3,2,2])) #4



# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def fn(nums):
    l=0
    maxfruits=0
    basket={}
    for r in range(len(nums)):
        basket[nums[r]] = basket.get(nums[r],0)+1
        if len(basket)>2:
            basket[nums[l]]-=1
            if basket[nums[l]]==0:
                del basket[nums[l]]
            l+=1
        maxfruits=max(maxfruits,r-l+1)
    return maxfruits
print(fn([1,2,1])) #3
print(fn([1,2,3,2,2])) #4