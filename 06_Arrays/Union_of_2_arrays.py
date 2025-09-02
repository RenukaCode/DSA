# Using set(both for sorted and unsorted arrays)
# Time Complexity; O((n+m) log(n+m)) → because of sorting 
# Space Complexity: O(m + n)
def unionfinding(arr1, arr2):
    union = set()
    s = arr1 + arr2
    for nums in s:
        union.add(nums)
    return sorted(union)
print(unionfinding([1,2,3,4,5], [3,4,5,6,7]))
# [1, 2, 3, 4, 5, 6, 7]
print(unionfinding([10,20,30], [20,20,20,50]))
# [10, 20, 30, 50]
print(unionfinding([1,2,2,1,0], [34,1,0]))
# [0, 1, 2, 34]
    


# Using map(both for sorted and unsorted arrays)
# Time Complexity: O((m + n)log(n + m)) → because of sorting 
# Space Complexity: O(m + n)
def unionFinding(arr1, arr2):
    freq = {}
    union = []
    for  nums in arr1:
        if nums in freq:
            continue
        else:
            freq[nums] = 1
    for nums in arr2:
        if nums in freq:
            continue
        else:
            freq[nums] = 1
    for nums in freq:
        union.append(nums)
    return sorted(union)
print(unionFinding([1,2,3,4,5], [3,4,5,6,7]))
# [1, 2, 3, 4, 5, 6, 7]
print(unionFinding([10,20,30], [20,20,20,50]))
# [10, 20, 30, 50]
print(unionFinding([1,2,2,1,0], [34,1,0]))



# Using 2 pointer approach(only for sorted arrays)
# Time Complexity: O(m + n)
# Space Complexity: O(m + n)
def unionFinding(arr1, arr2):
    i, j = 0, 0
    union = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
        else:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
            j += 1
    while i < len(arr1):
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
    while j < len(arr2):
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1
    return union
print(unionFinding([1,2,3,4,5], [3,4,5,6,7]))
# [1, 2, 3, 4, 5, 6, 7]
print(unionFinding([10,20,30], [20,20,20,50]))
# [10, 20, 30, 50]
    
                