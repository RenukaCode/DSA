# Time Complexity: O(n)
# Space Complexity: O(n)
def getPriority(c):
    if c == '^':
        return 3
    elif c in ('*', '/'):
        return 2
    elif c in ('+', '-'):
        return 1
    return 0

def infix_to_prefix(infix):
    st = []
    infix = '(' + infix + ')'
    res = ""
    for c in infix:
        if c.isalnum():
            res += c
        elif c == '(':
            st.append(c)
        elif c == ')':
            while st and st[-1] != '(':
                res += st.pop()
            st.pop()
        else:  # operator
            while st and getPriority(c) <= getPriority(st[-1]):
                res += st.pop()
            st.append(c) 
    return res

def infix_to_postfix(infix):
    infix = infix[::-1]
    infix = infix.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    prefix = infix_to_prefix(infix)
    return prefix[::-1]

print("Prefix:", infix_to_postfix("(p+q)*(c-d)"))   # *+pq-cd
print("Postfix:", infix_to_prefix("(p+q)*(c-d)"))   # pq+cd-*
