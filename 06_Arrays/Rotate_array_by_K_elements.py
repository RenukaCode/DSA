# Time Complexity: O(N)
# Space COmplexity: O(N)

# for left rotation
def rotate(arr, n, k):
    temp = arr[:k]
    res = arr[k:]
    return res + temp
print(rotate([1,2,3,4,5], 5, 2))
# [3, 4, 5, 1, 2]   
print(rotate([1,2,3,4,5], 5, 3))
# [4, 5, 1, 2, 3]

# for right rotation
def rotate(arr, n, k):
    temp = arr[-k:]
    res = arr[:-k]
    return temp + res
print(rotate([1,2,3,4,5], 5, 2))
# [4, 5, 1, 2, 3]
print(rotate([1,2,3,4,5], 5, 3))
# [3, 4, 5, 1, 2]
