# Brute Force Approach
# Time Complexity: O(N^4)
# Space Complexity: O(2*no. of quadruplets)
def quads(nums, target):
    n = len(nums)
    st = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()
                        st.add(tuple(temp))

    ans = [list(t) for t in st]
    ans.sort()
    return ans
print(quads([1,0,-1,0,-2,2], 0))
# [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(quads([4,3,3,4,4,2,1,2,1,1],9))
# [[1, 1, 3, 4], [1, 2, 2, 4], [1, 2, 3, 3]]



# Better Approach
# Time Complexity: O(N^3*log(M))
# Space Complexity: O(2 * no. of the quadruplets) + O(N)
def quads(nums, target):
    st = set()
    n = len(nums)
    for i in range(n):   
        for j in range(i + 1, n):
            hashSet = set()
            for k in range(j + 1, n):
                fourth = target - (nums[i] + nums[j] + nums[k])
                if fourth in hashSet:
                    temp = [nums[i] , nums[j], nums[k], fourth]
                    temp.sort()
                    st.add(tuple(temp))
                hashSet.add(nums[k])
    ans = [list(t) for t in st]
    ans.sort()
    return ans
print(quads([1,0,-1,0,-2,2], 0))
#  [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(quads([4,3,3,4,4,2,1,2,1,1],9))
#  [[1, 1, 3, 4], [1, 2, 2, 4], [1, 2, 3, 3]]



# Optimal Approach
# Time Complexity: O(N^3)
# Space Complexity: O(no. of quadruplets)
def quads(nums, target):
    n = len(nums)
    nums.sort()
    ans = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left = j + 1
            right = n - 1
            while left < right:
                sum_ = nums[i] + nums[j] + nums[left] + nums[right]
                if sum_ < target:
                    left += 1
                elif sum_ > target:
                    right -= 1
                else:
                    temp = [nums[i], nums[j], nums[left], nums[right]]
                    ans.append(temp)
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
    return ans
print(quads([1,0,-1,0,-2,2], 0))
#  [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(quads([4,3,3,4,4,2,1,2,1,1],9))
#  [[1, 1, 3, 4], [1, 2, 2, 4], [1, 2, 3, 3]]

                    