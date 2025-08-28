def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)
    
    
def merge(left, right):
    res = []
    i = j = 0
    while(i < len(left) and j < len(right)):
        if(left[i] <= right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
    
print(mergeSort([5, 4, 3, 2, 1])) #[1, 2, 3, 4, 5]
print(mergeSort([13,46,24,52,20,9])) #[9, 13, 20, 24, 46, 52]