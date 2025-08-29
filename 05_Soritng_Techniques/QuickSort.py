#Time Complexity: O(n log n) on average, O(n^2) in the worst case
#Space Complexity: O(log n) due to recursion stack

def partition(arr, lo, hi):
    pivot = arr[lo]            
    i = lo - 1
    j = hi + 1
    
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quicksort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p)       
        quicksort(arr, p + 1, hi)   

def quick_sort(arr):
    quicksort(arr, 0, len(arr) - 1)
    return arr


print(quick_sort([8, 3, 7, 6, 2, 5, 4, 1])) #[1, 2, 3, 4, 5, 6, 7, 8]
print(quick_sort([13, 46, 24, 52, 20, 9])) #[9, 13, 20, 24, 46, 52]



        
