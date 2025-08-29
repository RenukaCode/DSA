# Time COmplexity: O(n²)
# Space Complexity: O(n)                

def insertionSort(arr, i, n):
    if i == n:
        return arr
    
    j = i
    while j > 0 and arr[j] < arr[j - 1]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j -= 1 
    insertionSort(arr, i + 1, n)
    return arr
print(insertionSort([5, 4, 3, 2, 1], 1, 5)) #[1, 2, 3, 4, 5]
print(insertionSort([13,46,24,52,20,9], 1, 6)) #[9, 13, 20, 24, 46, 52]

