# Brute Force Approach
# Time Complexity: O(O(n+m) + O(n+m))
# Space Complexity: O(n + m)
def merge(arr1, arr2, m, n):
    arr3 = [0] * (m + n)
    left = 0
    right = 0
    index = 0
    while left < m and right < n:
        if arr1[left] <= arr2[right]:
            arr3[index] = arr1[left]
            left += 1
        else:
            arr3[index] = arr2[right]
            right += 1
        index += 1
    while left < m:
        arr3[index] = arr1[left]
        left += 1
        index += 1
    while right < n:
        arr3[index] = arr2[right]
        right += 1
        index += 1
    return arr3

print(merge([1, 4, 8, 10], [2, 3, 9], 4, 3))  # Output: [1, 2, 3, 4, 8, 9, 10]



