# Time Complexity: O(N)
# Space Complexity: O(n)

def countEle(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for key, value in freq.items():
        print(f"{key}: {value}")
# example
countEle([10, 5, 10, 15, 10, 5]) 
# 10: 3
# 5: 2
# 15: 1
countEle([7, 3, 2, 7, 4])
# 7: 2
# 3: 1
# 2: 1
# 4: 1
