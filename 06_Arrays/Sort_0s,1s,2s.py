# Better Appraoch
# Time Complexity: O(2N)
# Space Complexity: O(1)
def sortArray(arr, n):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for i in arr:
        if i == 0:
            count_0 += 1
        elif i == 1:
            count_1 += 1
        else: 
            count_2  += 1
    for i in range(count_0):
        arr[i] = 0
    for i in range(count_0, count_0 + count_1):
        arr[i] = 1
    for i in range(count_0 + count_1, n):
        arr[i] = 2
    return arr
print(sortArray([0, 2, 1, 2, 0, 1], 6))
#  output: [0, 0, 1, 1, 2, 2]
print(sortArray([0], 1))
#  output: [0]



# Optimal Approach
# Time Complexity: O(N)
# Space Complexity: O(1)
def sortArray(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums
print(sortArray([0, 2, 1, 2, 0, 1]))
# output: [0, 0, 1, 1, 2, 2]




