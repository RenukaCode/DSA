# Time Complexity: O(N)
# Space COmplexity: O(N)

arr = [4, 2, 4, 2, 6, 9, 6]
queries = [3, 8, 5, 2, 4, 6]
freq = {}
for nums in arr:
    if nums in freq:
        freq[nums] += 1
    else:
        freq[nums] = 1
for q in queries:
    print(freq.get(q, 0))
# o/p:
    # 0
    # 0
    # 0
    # 2
    # 2
    # 2

import re
s = "FUCK_PROCRASTINATION"
s = re.sub('[^a-zA-Z0-9]', '', s).lower()
freq = {}
for l in s:
    if l in freq:
        freq[l] += 1
    else:
        freq[l] = 1
for char, count in freq.items():
    print(f"{char}: {count}")
# o/p:
    # f: 1
    # u: 1
    # c: 2
    # k: 1
    # p: 1
    # r: 2
    # o: 2
    # a: 2
    # s: 1
    # t: 2
    # i: 2
    # n: 2

 
import re
s = "Coding is powerful and coding is fun"
s = re.sub('[^a-zA-Z0-9\s]', '', s).lower()
words = s.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
for char, count in freq.items():
    print(f"{char}: {count}")
# o/p:
    # coding: 2
    # is: 2
    # powerful: 1
    # and: 1
    # fun: 1

