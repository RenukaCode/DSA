# Time Complexity: O(n)
# Space Complexity: O(n)
def fn(tasks,n):
    maxFreq=0
    maxCnt=0
    freq={}
    for i in tasks:
        freq[i]=freq.get(i,0)+1
        maxFreq=max(freq.values())
        maxCnt=sum(1 for v in freq.values() if v==maxFreq)
    return max((maxFreq-1)*(n+1)+maxCnt,len(tasks))
print(fn(["A","A","A","B","B","B"],2))  # 8
print(fn(["A","A","A","B","B","B"],0))  # 6
print(fn(["A","C","A","B","D","B"],1))  # 6

