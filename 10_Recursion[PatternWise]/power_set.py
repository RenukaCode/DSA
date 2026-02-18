# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)
def fn(s):
    n = len(s)
    total = 1<<n
    subsequences = []
    for mask in range(1,total):
        subseq = []
        for i in range(n):
            if mask & (1<<i):
                subseq.append(s[i])
        subsequences.append(''.join(subseq))
    return subsequences
print(fn("abc"))
# ['a', 'b', 'ab', 'c', 'ac', 'bc', 'abc']
print(fn("aa"))
# ['a', 'a', 'aa']



# Recursive way
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)
def helper(s,index,curr,res):
    if index == len(s):
        res.append("".join(curr))
        return
    helper(s,index+1,curr,res)
    curr.append(s[index])
    helper(s,index+1,curr,res)
    curr.pop()
def getsubsequences(s):
    res = []
    curr = []
    helper(s,0,curr,res)
    return res
print(getsubsequences("abc"))
# ['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc']
print(getsubsequences("aa"))
# ['', 'a', 'a', 'aa']

