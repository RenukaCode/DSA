# Brute Force Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def fn(nums):
    ans = []
    mpp = {}
    for num in nums:
        mpp[num] = mpp.get(num,0)+1
    for key, value in mpp.items():
        if value == 1:
            ans.append(key)
    ans.sort()
    return ans
print(fn([1,2,1,3,5,2])) #[3,5]
print(fn([-1,0])) #[-1,0]