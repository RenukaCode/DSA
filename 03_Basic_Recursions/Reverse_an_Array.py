# Recursive Method
# Time Complexity: O(N)
# Space Complexity: O(1)

def reverse_array(arr, left, right):
    n = len(arr)
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse_array(arr, left + 1, right - 1)
arr = [10, 20, 30, 40, 50]
reverse_array(arr, 0, len(arr) - 1)
print(arr)   # [50, 40, 30, 20, 10]



# Iterative Method
# Time Complexity: O(N)
# Space Complexity: O(N)

def reverse_array(arr, left, right):
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
    if left >= right:
        return
arr = [5, 4, 3, 2, 1]
reverse_array(arr, 0, len(arr) - 1)
print(arr)   # [1, 4, 3, 2, 5]
    
   