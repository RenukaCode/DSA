# Brute Force Approach
# Time Complexity: O(N²)
# Space Complexity: O(1)
def fn(nums):
    n=len(nums)
    mod = int(1e9+7)
    total = 0
    for i in range(n):
        mini = nums[i]
        for j in range(i,n):
            mini = min(mini, nums[j])
            total = (total+mini)%mod
    return total
print(fn([3,1,2,5]))  #18
print(fn([2,3,1]))    #10



# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def fn(nums):
    n=len(nums)
    res = [0]*n
    st = []
    for i in range(n):
        while st and nums[st[-1]] > nums[i]:
            st.pop()
        j=st[-1] if st else -1
        res[i]=res[j]+(i-j)*nums[i]
        st.append(i)
    return sum(res)%(10**9+7)
print(fn([3,1,2,5]))  #18
print(fn([2,3,1]))    #10