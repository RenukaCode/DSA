# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(k)
def fn(s,k):
    maxlen=0
    for i in range(len(s)):
        freq={}
        for j in range(i,len(s)):
            freq[s[j]] = freq.get(s[j],0)+1
            if len(freq)>k:
                break
            maxlen = max(maxlen,j-i+1)
    return maxlen
print(fn("eceba",2))         # 3
print(fn("aababbcaacc",2))   # 6
print(fn("abcddefg",3))      # 4



# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(k)
def fn(s,k):
    if k==0 or not s:
        return 0
    maxlen=0
    l=0
    freq={}
    for r in range(l,len(s)):
        freq[s[r]] = freq.get(s[r],0)+1
        while len(freq)>k:
            freq[s[l]] -= 1
            if freq[s[l]] == 0:
                del freq[s[l]]
            l+=1
        maxlen=max(maxlen,r-l+1)
    return maxlen
print(fn("eceba",2))          # 3
print(fn("aababbcaacc",2))    # 6
print(fn("abcddefg",3))       # 4
print(fn("a,c,d",0))          # 0

