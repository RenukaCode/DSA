# Brute Force Approach
# Time Complexity: O(N²)
# Space Complexity: O(1)
def fn(nums,n):
    res=[0]*n
    for i in range(n):
        curr=0
        for j in range(i,-1,-1):
            if nums[j] <= nums[i]:
                curr+=1
            else:
                break
        res[i]=curr
    return res
print(fn([120, 100, 60, 80, 90, 110, 115],7))   #[1, 1, 1, 2, 3, 5, 6]
print(fn([15, 13, 12, 14, 16, 20],6))    #[1, 1, 1, 3, 5, 6]



# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def findPge(arr):
    n=len(arr)
    res=[0]*n
    st=[]
    for i in range(n):
        curr=arr[i]
        while st and arr[st[-1]] <= curr:
            st.pop()
        if not st:
            res[i]=-1
        else:
            res[i]=st[-1]
        st.append(i)
    return res
def fn(arr,n):
    pge=findPge(arr)
    res=[0]*n
    for i in range(n):
        res[i]=i-pge[i]
    return res
print(fn([120, 100, 60, 80, 90, 110, 115],7))   #[1, 1, 1, 2, 3, 5, 6]
print(fn([15, 13, 12, 14, 16, 20],6))    #[1, 1, 1, 3, 5, 6]