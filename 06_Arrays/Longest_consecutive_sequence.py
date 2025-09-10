def longestConsecutive(nums):
    n = len(nums)
    maxLen = 0
    for i in range(n):
        x = nums[i]
        count = 1
        while True:
            found = False
            for j in range(n):
                if nums[j] == x + 1:
                    count += 1
                    x = nums[j]
                    found = True
                    break
            if not found:
                break
        maxLen = max(maxLen, count)
    return maxLen
print(longestConsecutive([100, 4, 200, 1, 3, 2]))
# output: 4
print(longestConsecutive([3, 8, 5, 7, 6]))
#  output: 4



def longestConsecutive(nums):
    n = len(nums)
    if n == 0:
        return 0
    nums.sort()
    lastEle = float('-inf')
    count = 0
    longest = 1
    for i in range(n):
        if nums[i] - 1 == lastEle:
            count += 1
            lastEle = nums[i]
        elif nums[i] != lastEle:
            count = 1
            lastEle = nums[i]
        longest = max(longest, count)
    return longest
print(longestConsecutive([100, 4, 200, 1, 3, 2]))
# output: 4
print(longestConsecutive([3, 8, 5, 7, 6]))
#  output: 4


def longestConsecutive(nums):
    if not nums:
        return 0
    num_set = set(nums)
    longest = 0
    for x in num_set:
        if x - 1 not in num_set:
            count = 1
            cur = x
            while cur + 1 in num_set:
                cur += 1
                count += 1
        longest = max(longest, count)
    return longest
print(longestConsecutive([100,4,200,1,3,2]))
# output: 4
print(longestConsecutive([3,8,5,7,6]))
# output: 4
