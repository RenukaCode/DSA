# Brute Force Aproach
# Time Complextiy: O(n log n)
# Space Complexity: O(n)
def largest(arr):
    arr.sort()
    return arr[-1]
print(largest([2, 5, 1, 9, 4, 1])) # Output: 9

#  Recursive Approach
# Time Complexity: O(n)
# Space COmplexity: O(1)
def largest(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max
print(largest([4, 76, 243, 67, 2334, 75, 2])) # Output: 2334
print(largest([-4, -76, -243, -67, -2334, -75, -2])) # Output: -2


