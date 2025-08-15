# link:  https://leetcode.com/problems/two-sum/

# Time Complexity: O(n)
# Space Complexity: O(n)

def two_sum(nums, target):
    res = {}
    for i in range(len(nums)):
        j = target - nums[i]
        if j in res:
            return [res[j], i]
        res[nums[i]] = i
    return []

# Example:
print(two_sum([11, 15, 2, 7], 9))  
# o/p : [2, 3]
print(two_sum([11, 15], 9))
# o/p : []

