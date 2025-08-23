# Time Complexity: O(N)
# Space Complexity: O(N)
def countEle(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    maxFreq = float('-inf')
    maxEle = None
    minFreq = float('inf')
    minEle = None
    for num, count in freq.items():
        if count > maxFreq:
            maxFreq = count
            maxEle = num
        if count < minFreq:
            minFreq = count
            minEle = num
    print(maxEle, minEle)
countEle([10, 5, 10, 15, 10, 5])
#  10 15
countEle([7, 3, 2, 7, 4])
#  7 3