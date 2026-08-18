# Time Complexity: O(n)
# Space Complexity: O(1)
def isMinHeap(nums):
    n=len(nums)
    for i in range(n//2):
        left=2*i+1
        if left < n and nums[i] > nums[left]:
            return False
        right=2*i+2
        if right < n and nums[i] > nums[right]:
            return False
    return True
print(isMinHeap([10, 20, 30, 21, 23]))  # True
print(isMinHeap([10, 20, 30, 25, 15]))  # False