# Brute Force Approach
# Time Complexity: O(N1+N2)
# Space Complexity: O(N1+N2)
def median(nums1, nums2):
    arr = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums1[j]:
            arr.append(nums1[i])
            i += 1
        else:
            arr.append(nums2[j])
            j += 1
    arr += nums1[i:]
    arr += nums2[j:]

    n = len(arr)
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2.0
print(median([1, 3],[2]))
# 2
print(median([2,4,6],[1,3,5]))
# 3.5
print(median([2,4,6],[1,3]))
# 3



# Better Approach
# Time Complexity: O(N1+N2)
# Space Complexity: O(1)
def median(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    n = n1 + n2
    ind2 = n // 2
    ind1 = ind2 - 1
    indELe1 = indEle2 = -1
    i = j = count = 0
    while i < n1 and j < n2:
        if nums1[i] < nums2[j]:
            if count == ind1: indELe1 = nums1[i]
            if count == ind2: indEle2 = nums1[i]
            i += 1
        else:
            if count == ind1: indEle1 = nums2[j]
            if count == ind2: indEle2 = nums2[j]
            j += 1
        count += 1
    while i < n1:
        if count == ind1: indELe1 = nums1[i]
        if count == ind2: indEle2 = nums1[i]
        i += 1
        count += 1
    while j < n2:
        if count == ind1: indEle1 = nums2[j]
        if count == ind2: indEle2 = nums2[j]
        j += 1
        count += 1
    if n % 2 == 1:
        return float(indEle2)
    return (indEle1 + indEle2) / 2.0
print(median([1, 3],[2]))
# 2.0
print(median([2,4,6],[1,3,5]))
# 3.5
print(median([2,4,6],[1,3]))
# 3.0
