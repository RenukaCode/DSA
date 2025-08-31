# BruteForce Approach
# Time Complexity: O(nlogn)
# Space COmplexity: O(1)
def elements(arr):
    arr.sort()
    return arr[1], arr[-2]
print(elements([2, 5, 1, 9, 4])) # Output: (2, 5)



# Better Approach
# Time Complexity: O(n)
# Space COmplexity: O(1)
# Traverse the array twice. One is for finding small, large and another for 2nd small, 2nd large
def elements(arr):
    if len(arr) <= 2:
        return -1
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')
    for i in range(len(arr)):
        small = min(arr[i], small)
        large = max(arr[i], large)
    for i in range(len(arr)):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    return second_small, second_large
print(elements([2, 5, 1, 9, 4])) 
# Output: (2, 5)
print(elements([4, 76, 243, 67, 2334, 75, 2])) 
# Output: (4, 243)
print(elements([-4, -76, -243, -67, -2334, -75, -2])) 
# Output: (-243, -4)



# Optimal Approach
# Time Complexity: O(n)
# Space COmplexity: O(1)
def elements(arr):
    if (len(arr) <= 2):
        return -1
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')
    for i in range(len(arr)):
        if arr[i] < small:
            second_small = small
            small = arr[i]
        if arr[i] > large:
            second_large = large
            large = arr[i]
    return second_small, second_large
print(elements([2, 5, 1, 9, 4])) 
# Output: (2, 5)
print(elements([2, 5])) 
# Output: -1