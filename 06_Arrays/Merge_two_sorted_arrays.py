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
print(merge([1, 4, 8, 10], [2, 3, 9], 4, 3))  
# Output: [1, 2, 3, 4, 8, 9, 10]



# Optimal Approach 1
# Time Complexity:  O(min(n, m)) + O(n*logn) + O(m*logm)
# Space Complexity: O(1)
def merge(arr1, arr2, m, n):
    left = m - 1
    right = 0
    while left >= 0 and right < n:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
        left -= 1
        right += 1
    arr1.sort()
    arr2.sort()
    return arr1 + arr2
print(merge([1, 4, 8, 10], [2, 3, 9], 4, 3))  
# Output: [1, 2, 3, 4, 8, 9, 10]


# Time Complexity: O(nlogn)
# Space Complexity: O(m + n)
def merge(arr1, arr2, m, n):
    merged = arr1 + arr2
    merged.sort()
    return merged
print(merge([1, 4, 8, 10], [2, 3, 9], 4, 3))
# Output: [1, 2, 3, 4, 8, 9, 10]


       
    