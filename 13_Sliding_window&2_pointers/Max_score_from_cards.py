# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def fn(cards,k):
    n=len(cards)
    maxSum=0
    for i in range(k+1):
        tempSum=0
        for j in range(i):
            tempSum+=cards[j]
        for j in range(k-i):
            tempSum+=cards[n-1-j]
        maxSum=max(maxSum,tempSum)
    return maxSum
print(fn([1,2,3,4,5,6],3))        # 15
print(fn([5,4,1,8,7,1,3],3))      # 12



# Optimal Solution
# Time Complexity: O(k)
# Space Complexity: O(1)
def fn(cards,k):
    n=len(cards)
    total=sum(cards[:k])
    maxSum=total
    for i in range(k):
        total -= cards[k-1-i]
        total+=cards[n-1-i]
        maxSum = max(maxSum,total)
    return maxSum
print(fn([1,2,3,4,5,6],3))        # 15
print(fn([5,4,1,8,7,1,3],3))      # 12