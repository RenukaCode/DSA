# Time Complexity: O(n)
# Space Complexity: O(n)
def fn(nums):
    st = []
    n = len(nums)
    res = [0]*n
    for i in range(n-1,-1,-1):
        while st and st[-1] <= nums[i]:
            st.pop()
        if not st:
            res[i] = -1
        else:
            res[i] = st[-1]
        st.append(nums[i])
    return res
print(fn([4, 5, 2, 10]))  #[5, 10, 10, -1]
print(fn([1, 3, 2, 4]))   #[3, 4, 4, -1]
print(fn([6, 8, 0, 1, 3])) #[8, -1, 1, 3, -1]



# For two lists
# Time Complexity: O(n)
# Space Complexity: O(n)
def fn(nums1,nums2):
    st = []
    d = {}
    for i in nums2:
        while st and i > st[-1]:
            d[st.pop()] = i
        st.append(i)
    for i in st:
        d[i] = -1
    return [d[x] for x in nums1]
print(fn([4,1,2],[1,3,4,2]))  #[-1, 3, -1]