# Brute Force Approach
# Time Complexity: O(k*n) + O(n)
# Space Complexity: O(1)
def minimiseMaxDistance(arr, k):
    n = len(arr) 
    howMany = [0] * (n - 1)
    for gasStations in range(1, k + 1):
        maxSection = -1
        maxInd = -1
        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            sectionLength = diff / (howMany[i] + 1)
            if sectionLength > maxSection:
                maxSection = sectionLength
                maxInd = i
        howMany[maxInd] += 1
    maxAns = -1
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        sectionLength = diff / (howMany[i] + 1)
        maxAns = max(maxAns, sectionLength)
    return maxAns
print(minimiseMaxDistance([1, 2, 3, 4, 5],4))
# 0.5
print(minimiseMaxDistance([1,2,3,4,5,6,7,8,9,10],1, 1e-6))
# 1


# Optimal Solution
# Time Complexity:  O(n*log(Len)) + O(n)
# Space Comlexity: O(1)
import math
def minimiseMaxDistance(stations, k, eps):
    maxGap = max(stations[i + 1] - stations[i] for i in range(len(stations) - 1))
        
    low , high = 0.0, maxGap
    while high - low > eps:
        mid = (low + high) / 2.0
        required = 0
        for i in range(len(stations) - 1):
            gap = stations[i + 1] - stations[i]
            required += math.ceil(gap / mid) - 1
        if required > k:
            low = mid
        else:
            high = mid
    return high
print(minimiseMaxDistance([1, 2, 3, 4, 5],4, 1e-6))
# 0.5
print(minimiseMaxDistance([1,2,3,4,5,6,7,8,9,10],1, 1e-6))
# 1
