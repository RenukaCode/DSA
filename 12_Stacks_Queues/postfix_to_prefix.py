def postfix_to_prefix(postfix):
    st = []
    for c in postfix:
        if c.isalnum():
            st.append(c)
        else:
            op2 = st.pop()
            op1 = st.pop()
            st.append(c+op1+op2)
    return st[-1]
print(postfix_to_prefix("abc*+d-"))        # -+a*bcd
print(postfix_to_prefix("ABC/-AK/L-*"))    #*-A/BC-/AKL