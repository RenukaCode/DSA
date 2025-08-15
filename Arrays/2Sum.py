def two_sum(nums, target):
    res = {}
    for i in range(len(nums)):
        j = target - nums[i]
        if j in res:
            return [res[j], i]
        res[nums[i]] = i
    return []

# print(two_sum([11, 15, 2, 7], 9))
print(two_sum([11, 15], 9))

