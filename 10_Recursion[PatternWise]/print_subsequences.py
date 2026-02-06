# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)
def helper(s,idx,curr,res):
    if idx == len(s):
        res.append("".join(curr))
        return
    helper(s,idx+1,curr,res)
    curr.append(s[idx])
    helper(s,idx+1,curr,res)
    curr.pop()
def getSubsequences(s):
    res = []
    curr = []
    helper(s,0,curr,res)
    return res
s = "abc"
print(getSubsequences(s))   #['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc']
s = "abcd"
print(getSubsequences(s))   #['', 'd', 'c', 'cd', 'b', 'bd', 'bc', 'bcd', 'a', 'ad', 'ac', 'acd', 'ab', 'abd', 'abc', 'abcd']