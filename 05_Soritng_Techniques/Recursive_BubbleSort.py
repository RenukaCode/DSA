# Time Complexity:  O(n²)
# Space Complexity: O(n)

def bubbleSort(arr, n):
    if n == 1:
        return arr
    for i in range(n - 1):
        if arr[i]> arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    bubbleSort(arr, n - 1)
    return arr
print(bubbleSort([5, 4, 3, 2, 1], 5)) #[1, 2, 3, 4, 5]
print(bubbleSort([13,46,24,52,20,9], 6)) #[9, 13, 20, 24, 46, 52]


# Time Complexity: O(n²)
# Space Complexity: O(n)
def bubbleSort(arr, n):
    if n <= 1:
        return arr
    swapped = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
    return arr if not swapped else bubbleSort(arr, n - 1)
print(bubbleSort([5, 4, 3, 2, 1], 5)) #[1, 2, 3, 4, 5]
print(bubbleSort([13,46,24,52,20,9], 6)) #[9, 13, 20, 24, 46, 52]
    


