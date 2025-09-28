# Brute Force Approach
# Time COmplexity: O(N^2)
# Space Complexity: O(1)
def reversePairs(nums, n):
    count =  0
    for i in range(n):
        for j in range(i + 1, n):
            if i < j and nums[i] > 2 * nums[j]:
                count += 1
    return count
print(reversePairs([1,3,2,3,1], 5))
# 2
print(reversePairs([2,4,3,5,1], 5))
# 3


def merge(nums, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1
    while left <= mid:
        temp.append(nums[left])
        left += 1
    while right <= high:
        temp.append(nums[right])
        right += 1
    for i in range(low, high + 1):
        nums[i] = temp[i - low]
def countPairs(nums, low, mid, high):
    right = mid + 1
    count = 0
    for i in range(low, mid + 1):
        while right <= high and nums[i] > 2 * nums[right]:
            right += 1
        count += (right - (mid + 1))
    return count
def mergeSort(nums, low, high):
    count = 0
    if low >= high:
        return count
    mid = (low + high) // 2
    count += mergeSort(nums, low, mid)
    count += mergeSort(nums, mid + 1, high)
    count += countPairs(nums, low, mid, high)
    merge(nums, low, mid, high)
    return count
print(mergeSort([1,3,2,3,1], 0, len([1,3,2,3,1]) - 1))
# 2
print(mergeSort([2,4,3,5,1], 0, len([2,4,3,5,1]) - 1))
# 3
 
