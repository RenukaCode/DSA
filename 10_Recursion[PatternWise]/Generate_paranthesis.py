# Brute Force Approach
# Time Complexity: O(2^(2n) * n) 
# Space Complexity: O(n)
def isValid(s):
    cnt = 0
    for c in s:
        if c == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0
def generateAll(curr,n,res):
    if len(curr) == 2*n:
        if isValid(curr):
            res.append(curr)
        return
    generateAll(curr+'(',n,res)
    generateAll(curr+')',n,res)
def generatePara(n):
    res = []
    generateAll("",n,res)
    return res
n = 3
print(generatePara(n))   #['((()))', '(()())', '(())()', '()(())', '()()()']
n = 4
print(generatePara(n))   #['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']



# Optimal Approach
# Time Complexity: O(2^n)
# Space Complexity: O(n)
def fn(curr,open,close,n,res):
    if len(curr) == 2*n:
        res.append(curr)
    if open < n:
        fn(curr + '(',open+1,close,n,res)
    if close < open:
        fn(curr + ')',open,close+1,n,res)
def generateParas(n):
    res = []
    fn("",0,0,n,res)
    return res
n = 3
print(generateParas(n))   #['((()))', '(()())', '(())()', '()(())', '()()()']
n = 4
print(generateParas(n))   #['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']
