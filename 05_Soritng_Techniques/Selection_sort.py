# Time Complexity: O(n²)
# Space Complexity: O(1)

def selectionSort(arr):
    n = len(arr)
    temp = None
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
print(selectionSort([5,4,3,2,1]))
print(selectionSort([13,46,24,52,20,9]))


