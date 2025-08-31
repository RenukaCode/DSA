# Brute Force Approach:
# TIme Complexity: O(nlogn)
# Space COmplexity: O(1)
def checking(arr):
    if len(arr) == 0 or len(arr) == 1:
        return True
    sortedArr = sorted(arr)
    if sortedArr == arr:
        return True
    return False
print(checking([1, 2, 3, 4, 5])) # Output: True
print(checking([1, 3, 2, 4, 5])) # Output: False
print(checking([])) # Output: True



# Brute Force Approach:
# TIme Complexity: O(n^2)
# Space COmplexity: O(1)
def checking(arr):
    if len(arr) == 0 or len(arr) == 1:
        return True
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                return False
    return True
print(checking([1, 2, 3, 4, 5])) # Output: True
print(checking([6, 3, 8, 2, 7])) # Output: False
print(checking([])) # Output: True




# Optimal solution:
# Time Complexity: O(n)
# Space Complexity: O(1)
def checking(arr):
    if len(arr) == 0 or len(arr) == 1:
        return True
    for i in range(0, len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            continue
        else:
            return False
    return True
print(checking([1, 2, 3, 4, 5])) #True
print(checking([1, 3, 2, 4, 5])) #False
print(checking([])) # Output: True
print(checking([1])) # Output: True