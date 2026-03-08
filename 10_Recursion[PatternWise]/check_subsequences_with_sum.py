# Time Complexity: O(2^n)
# Space Complexity: O(n)
def fn(i,n,arr,k):
    if k == 0:
        return True
    if k < 0:
        return False
    if i == n:
        return k == 0
    return fn(i+1,n,arr,k) or fn(i+1,n,arr,k-arr[i])
def checkSubsequences(arr,k):
    n = len(arr)
    return fn(0,n,arr,k)
# print(checkSubsequences([1,2,3,4,5],8)) # True
print(checkSubsequences([4,3,9,2],10)) # False
