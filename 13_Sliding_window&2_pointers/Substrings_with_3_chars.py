# Brute Force Approach
# Time Complexity: O(n²)
# Space Complexity:O(1)
def fn(s):
    cnt=0
    n=len(s)
    for i in range(n):
        freq={'a':0,'b':0,'c':0}
        for j in range(i,n):
            freq[s[j]] += 1
            if freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                cnt += 1
    return cnt
print(fn("abcabc")) #10
print(fn("ccabcc")) #8



# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def fn(s):
    freq=[0,0,0]
    left=0
    res=0
    for right in range(len(s)):
        freq[ord(s[right])-ord('a')]+=1
        while freq[0]>0 and freq[1]>0 and freq[2]>0:
            res+=len(s)-right
            freq[ord(s[left])-ord('a')] -= 1
            left+=1
    return res
print(fn("abcabc")) #10
print(fn("ccabcc")) #8