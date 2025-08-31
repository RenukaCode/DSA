# Brute Force Approach
# Time Complexity: O(n)
# Space COmplexity: O(n)
def leftRotate(arr):
    a = arr[0]
    nums = []
    for i in range(1, len(arr)):
        nums.append(arr[i])
    nums.append(a)
    return nums
print(leftRotate([1,2,3,4,5]))
# [2, 3, 4, 5, 1]
print(leftRotate([5,4,3,2,1])) 
# [4, 3, 2, 1, 5] 



# Optimal Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def leftRotate(arr):
    a = arr[0]
    for i in range(0, len(arr) - 1):
        arr[i] =arr[i + 1]
    arr[-1] = a
    return arr
print(leftRotate([1,2,3,4,5]))
# [2, 3, 4, 5, 1]
print(leftRotate([5,4,3,2,1])) 
# [4, 3, 2, 1, 5]
