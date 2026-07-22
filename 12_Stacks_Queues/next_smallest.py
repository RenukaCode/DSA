# Time Complexity: O(n*2)
# Space Complexity: O(n)
def fn(nums):
    n=len(nums)
    ans = [-1]*n
    for i in range(n):
        for j in range(i+1,n):
            if nums[j] < nums[i]:
                ans[i] = nums[j]
                break
    return ans
print(fn([1, 3, 2, 4]))  # [-1, 2, -1, -1]
print(fn([4, 8, 5, 2, 25]))   # [2, 5, 2, -1, -1]

