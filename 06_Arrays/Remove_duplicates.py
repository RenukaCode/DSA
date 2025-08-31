# Using Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)
def duplicates(arr):
    st = set()
    for i in range(len(arr)):
        st.add(arr[i])
    k = len(st)
    return k, st
print(duplicates([1,2,3,4,5,5,6,7,8,8,9]))
# (9, {1, 2, 3, 4, 5, 6, 7, 8, 9})
print(duplicates([1,1,1,1,1,1,1,1,1,1]))
# (1, {1})



#  without using Hash set / two pointers Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def remove_duplicates(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1, arr[: i + 1]
print(remove_duplicates([1,2,3,4,5,5,6,7,8,8,9]))
# (9, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(remove_duplicates([1,1,1,1,1,1,1,1,1,1]))
# (1, [1])




