# Time Complexity: O(N)
# Space COmplexity: O(1)
def count(nums):
    count = 0
    max_count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count = 0
        max_count = max(max_count, count)
    return max_count
print(count([1, 1, 0, 1, 1, 1]))  
# Output: 3
print(count([1, 0, 0, 1, 0]))        
# Output: 1
print(count([0, 0, 0]))              
# Output: 0
