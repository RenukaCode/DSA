# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def fn(s,k):
    maxlen=0
    for i in range(len(s)):
        freq=[0]*26
        maxfreq=0
        for j in range(i, len(s)):
            freq[ord(s[j])-ord('A')] += 1
            maxfreq=max(maxfreq,freq[ord(s[j])-ord('A')])
            windlen=j-i+1
            replace=windlen-maxfreq
            if replace<=k:
                maxlen=max(maxlen,windlen)
    return maxlen
print(fn("AABABBA",1)) #4
print(fn("BAABAABBBAAA",2)) #6



# Better Approach
# Time Complexity: O(n)
# Space Complexity: O(26)
def fn(s,k):
    freq={}
    left=0
    maxfreq=0
    maxlen=0
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right],0)+1
        maxfreq=max(maxfreq, freq[s[right]])
        while (right-left+1)-maxfreq>k:
            freq[s[left]]-=1
            left+=1
        maxlen=max(maxlen,right-left+1)
    return maxlen
print(fn("AABABBA",1)) #4
print(fn("BAABAABBBAAA",2)) #6



# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def fn(s,k):
    freq=[0]*26
    left=0
    maxcnt=0
    maxlen=0
    for right in range(len(s)):
        freq[ord(s[right])-ord('A')] += 1
        maxcnt=max(maxcnt,freq[ord(s[right])-ord('A')])
        while(right-left+1)-maxcnt>k:
            freq[ord(s[left])-ord('A')] -= 1
            left += 1
        maxlen=max(maxlen,right-left+1)
    return maxlen
print(fn("AABABBA",1)) #4
print(fn("BAABAABBBAAA",2)) #6
