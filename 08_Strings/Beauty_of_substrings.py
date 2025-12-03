# Time Complexity: O(n^2)
# Space Complexity: O(1)
def fn(s):
    n = len(s)
    total = 0
    for i in range(n):
        freq = {}
        for j in range(i, n):
            freq[s[j]] = freq.get(s[j], 0) + 1
            values = freq.values()
            maxi = max(values)
            mini = min(values)
            total += (maxi - mini)
    return total
print(fn("xyx"))
# 1
print(fn("aabcbaa"))
# 17

             