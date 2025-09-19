# Brute Force Approach
# Time COmplexity: O(N^2)
# Space Complexity: O(1)
def majorityEle(nums, n):
    res = []
    count = 0
    for i in range(n):
        for j in range(0, n):
            if nums[i] == nums[j]:
                count += 1
        if count > (n // 3):
            res.append(nums[i])
        if len(res) == 2:
            break
    return res
print(majorityEle([11,33,33,11,33,11], 6))
#  [11, 33]
            


# Better Approach
# Time Complexity: O(N)
# Space Complexity: O(N)
def majorityEle(nums, n):
    freq = {}
    res = []
    for i in range(n):
        if nums[i] in freq:
            freq[nums[i]] += 1
        else:
            freq[nums[i]] = 1
    for key, value in freq.items():
        if value > (n // 3):
            res.append(key)
    return res
print(majorityEle([1,2,2,3,2], 5))
# [2]
print(majorityEle([11,33,33,11,33,11], 6))
#  [11, 33]
        
        
