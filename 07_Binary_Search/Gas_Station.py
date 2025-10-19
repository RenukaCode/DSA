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
