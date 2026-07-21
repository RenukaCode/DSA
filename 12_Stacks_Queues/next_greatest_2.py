# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def fn(arr):
    n=len(arr)
    ans=[-1]*n
    for i in range(n):
        curr = arr[i]
        for j in range(1,n):
            idx = (j+i)%n
            if arr[idx] > curr:
                ans[i] = arr[idx]
                break
    return ans
print(fn( [5, 7, 1, 7, 6, 0]))   # [7, -1, 7, -1, 7, 5]



# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def fn(arr):
    n = len(arr)
    ans = [-1]*n
    st = []
    for i in range(2*n-1,-1,-1):
        idx = i%n
        curr = arr[idx]
        while st and st[-1] <= curr:
            st.pop()
        if i<n:
            if st:
                ans[i]=st[-1]
        st.append(curr)
    return ans
print(fn([5, 7, 1, 7, 6, 0]))  #[7, -1, 7, -1, 7, 5]
