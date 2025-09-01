# Time Complexity: O(n)
# Space Complexity: O(1)
def linearSearch(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i
    return None
print(linearSearch([1,2,3,4,5], 5, 3))
# 2
print(linearSearch([10,20,30,40,50], 5, 25))
# None