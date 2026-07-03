# Time Complexity: O(n)
# Space Complexity: O(n)
def fn(arr):
    st = set()
    for i in arr:
        if i in st:
            st.remove(i)
        else:
            st.add(i)
    return st.pop() if st else None
print(fn([2,2,1])) # 1
print(fn([4,1,2,1,2])) # 4



# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def fn(arr):
    xor = 0
    for i in arr:
        xor ^= i
    return xor
print(fn([2,2,1])) # 1
print(fn([4,1,2,1,2])) # 4
