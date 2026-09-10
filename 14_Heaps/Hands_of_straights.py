# Time Complexity: O(NLogN)
# Space Complexity: O(N)
from collections import Counter
import heapq
import heapq
def fn(hand,grpSize):
    if len(hand)%grpSize != 0:
        return False
    freq=Counter(hand)
    minheap=list(freq.keys())
    heapq.heapify(minheap)
    while minheap:
        first=minheap[0]
        for i in range(grpSize):
            card=first+i
            if freq[card]==0:
                return False
            freq[card]-=1
            if freq[card]==0 and card==minheap[0]:
                heapq.heappop(minheap)
    return True
print(fn([1,2,3,6,2,3,4,7,8],3))  # True
print(fn([1,2,3,4,5],4))  # False

