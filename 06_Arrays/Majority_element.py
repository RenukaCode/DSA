# Brute Force Approach
# Time COmplexity: O(N^2)
# Space COmplexity: O(1)
def majorityElement(nums, N):
    for i in range(N):
        count = 0
        for j in range(N):
            if nums[j] == nums[i]:
                count += 1
        if count > (N//2):
            return nums[i]
    return -1
print(majorityElement([2,2,1,1,1,2,2], 7))
#  output: 2
print(majorityElement([4,4,2,4,3,4,4,3,2,4], 10))
#  output: 4



# Better Approach
# Time Complexity: O(N*logN) + O(N)
# Space Complexity: O(N) 
def majorityElement(nums, N):
    freq = {}
    for i in range(N):
        if nums[i] in freq:
            freq[nums[i]] += 1
        else:
            freq[nums[i]] = 1
    for key, value in freq.items():
        if value > (N//2):
            return key
    return -1
print(majorityElement([2,2,1,1,1,2,2], 7))
#  output: 2
print(majorityElement([4,4,2,4,3,4,4,3,2,4], 10))
#  output: 4



# Optimal Approach
# Time Complexity: O(N) + O(N)
# Space Complexity: O(1)
def majorityElement(nums, N):
    count = 0
    ele = None
    for i in range(N):
        if count == 0:
            count = 1
            ele = nums[i]
        elif ele == nums[i]:
            count += 1
        else:
            count -= 1
    count = 0
    for i in range(N):
        if nums[i] == ele:
            count += 1
    if count > (N/2):
        return ele
    return -1
print(majorityElement([2,2,1,1,1,2,2], 7))
#  output: 2
print(majorityElement([4,4,2,4,3,4,4,3,2,4], 10))
#  output: 4
