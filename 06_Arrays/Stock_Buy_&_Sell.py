# Brute Force Approach
# Time complexity: O(n^2)
# Space Complexity: O(1)
def profit(nums,n):
    maxProfit = 0
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                maxCur = nums[j] - nums[i]
                maxProfit = max(maxProfit, maxCur)
    return maxProfit
print(profit([7,1,5,3,6,4], 6))
# output: 5
print(profit([7,6,4,3,1], 5))
# output: 0



# Optimal Solution
# Time Complexity; O(N)
# Space COmplexity: O(1)
def profit(nums, n):
    maxProfit = 0
    minPrice = float('inf')
    for i in range(n):
        minPrice = min(minPrice, nums[i])
        maxProfit = max(maxProfit, nums[i] - minPrice)
    return maxProfit
print(profit([7,1,5,3,6,4], 6))
# output: 5
print(profit([7,6,4,3,1], 5))
# output: 0


def profit(prices, n):
    maxProfit = 0
    for i in range(1, n):
        if prices[i] > prices[i - 1]:
            maxProfit += prices[i] - prices[i - 1]
    return maxProfit
print(profit([7,1,5,3,6,4], 6))
# output: 7
print(profit([7,6,4,3,1], 5))
# output: 0
print(profit([1,2,3,4,5], 5))
# output: 4