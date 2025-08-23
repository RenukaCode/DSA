# Time Complexity: O(n²)
# Space Complexity: O(1)
def insertionSort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] =nums[j]
            j -= 1
            nums[j + 1] = key
    return nums
print(insertionSort([5, 4, 3, 2, 1]))
print(insertionSort([13,46,24,52,20,9]))


