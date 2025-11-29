# Time Complexity: O(N logN)
# Space Complexity: O(N)
from collections import Counter
def fn(s):
    freq = Counter(s)
    sortedChars = sorted(freq.items(), key = lambda x: (-x[1], x[0]))
    res = []
    for i in sortedChars:
        res.append(i)
    return res
print(fn("tree"))
# ['e', 'r', 't']
print(fn("raaaajj"))
# ['a', 'j', 'r']
print(fn("cabv"))
# ['a', 'b', 'c', 'v']