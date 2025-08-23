# Time Complexity: O(n²)
# Space Complexity: O(1)

def bubbleSort(nums):
    n = len(nums)
    temp = None
    for i in range(0, n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
print(bubbleSort([13, 24, 46, 20, 9, 52]))
print(bubbleSort([5, 4, 3, 2, 1]))


