# Time Complexity: O(N)
# Space Complexity: O(N)
def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1
def fn(s):
    st = []
    res = ""
    for c in s:
        if c.isalnum():
            res += c
        elif c == '(':
            st.append('(')
        elif c == ')':
            while st and st[-1] != '(':
                res += st.pop()
            st.pop()
        else:
            while st and prec(c) <= prec(st[-1]):
                res += st.pop()
            st.append(c)
    while st:
        res += st.pop()
    return res
print(fn("(p+q)*(m-n)"))   # pq+mn-*