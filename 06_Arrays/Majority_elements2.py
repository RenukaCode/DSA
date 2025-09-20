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
        
        

def majorityEle(nums, n):
    count1 = 0
    count2 = 0
    el1 = float('-inf')
    el2 = float('-inf')
    for i in range(n):
        if count1 == 0 and el2 != nums[i]:
            count1 += 1
            el1 = nums[i]
        elif count2 == 0 and el1 != nums[i]:
            count2 += 1
            el2 = nums[i]
        else:
            count1 -= 1
            count2 -= 2
    res = []
    count1, count2 = 0, 0
    for i in range(n):
        if nums[i] == el1:
            count1 += 1
        if nums[i] == el2:
            count2 += 1
    
    mini = int(n/3) 
    if count1 > mini:
        res.append(el1)
    if count2 > mini:
        res.append(el2)
    return res
print(majorityEle([1,2,2,3,2], 5))
# [2]
print(majorityEle([11,33,33,11,33,11], 6))
#  [11, 33]