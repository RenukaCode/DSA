# Time Complexity: O(n)
# Space Complexity: O(n)
def postfix_to_infix(postfix):
    st = []
    for c in postfix:
        if c.isalnum():
            st.append(c)
        else:
            op2 = st.pop()
            op1 = st.pop()
            st.append(f"({op1}{c}{op2})")
    return st[-1]
print(postfix_to_infix("AB*C+"))  # ((A*B)+C)
print(postfix_to_infix("ab*cd/+")) #((a*b)+(c/d))