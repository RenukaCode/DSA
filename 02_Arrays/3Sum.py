# link:  https://leetcode.com/problems/3Sum/

# Two Pointer Approach:
def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)):
        if(i > 0 and nums[i] == nums[i - 1]):
            continue
        left = i + 1
        right = len(nums) - 1
        while(left < right):
            target = nums[i] + nums[left] + nums[right]
            if(target == 0):
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while(left < right and nums[left] == nums[left - 1]):
                    left += 1
                while(left < right and nums[right] == nums[right + 1]):
                    right -= 1
            elif(target < 0):
                left += 1
            else:
                right -= 1
    return res   
# example:   
print(threeSum([-1,0,1,2,-1,-4])) 
  # o/p: [[-1,-1,2],[-1,0,1]]

# Time Complexity: O(n^2)
# Space Complexity: O(1)