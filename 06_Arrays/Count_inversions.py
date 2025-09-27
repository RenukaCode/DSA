# Brute Force Approach
# Time Complexity: O(N^2)
# Space Complexity: O(1)
def inversions(nums, n):
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if i < j and nums[i] > nums[j]:
                count += 1
    return count
print(inversions([1,2,3,4,5], 5))
# 0
print(inversions([5,4,3,2,1], 5))
#  10
print(inversions([5,3,2,1,4], 5))
#  7



# Optimal Solution
# Time Complexity:  O(N*logN)
# Space Complexity: O(N)
def inversions(nums, low, mid, high):
    left = nums[low: mid + 1]
    right = nums[mid + 1: high + 1]
    i = j = 0
    k = low
    count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
            count += (len(left) - i)
        k += 1
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1
    return count
def mergeSort(nums, low, high):
    if low >= high:
        return 0
    mid = (low + high) // 2
    count = 0
    count += mergeSort(nums, low, mid)
    count += mergeSort(nums, mid + 1, high)
    count += inversions(nums, low, mid, high)
    return count
print(mergeSort([1,2,3,4,5], 0, len([1,2,3,4,5]) - 1))
# 0
print(mergeSort([5,4,3,2,1], 0, len([5,4,3,2,1])-1))
#  10
print(mergeSort([5,3,2,1,4], 0, len([5,3,2,1,4])-1))
#  7
