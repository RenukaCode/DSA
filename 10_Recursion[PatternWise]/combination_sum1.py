# Time Complexity: O(2^t*k)
# Space Complexity: O(k*x) where x is the number of combinations
def recFn(idx,target,arr,ans,ds):
    if idx == len(arr):
        if target == 0:
            ans.append(list(ds))
        return
    if arr[idx] <= target:
        ds.append(arr[idx])
        recFn(idx,target- arr[idx],arr,ans,ds)
        ds.pop()
    recFn(idx+1,target,arr,ans,ds)
def combinationSum(arr,target):
    ans = []
    ds = []
    recFn(0,target,arr,ans,ds)
    return ans
print(combinationSum([2,3,6,7],7)) # [[2,2,3],[7]]
print(combinationSum([2],1)) # []