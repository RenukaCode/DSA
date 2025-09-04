# Brute Force Approach
# TIme COmplexity: O(N^2)
# Space Complexity: O(1)
def numberOnce(arr):   
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count == 1:
            return arr[i]
print(numberOnce([1, 2, 3, 2, 1]))



# Better Approach using hashMap
# Time Complexity: O(N)
# Space Complexity: O(N)
def numberOnce(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for key, value in freq.items():
        if value == 1:
            return key
print(numberOnce([1, 2, 3, 2, 1]))
print(numberOnce([4, 5, 6, 5, 4, 6, 7]))



# Optimal Approach Using XOR
# Time Complexity: O(N)
# Space COmplexity: O(1)
def numberOnce(arr):
    xor = 0
    for i in arr:
        xor ^= i
    return xor
print(numberOnce([1, 2, 3, 2, 1]))


