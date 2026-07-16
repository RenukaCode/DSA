# Time Complexity: O(n)
# Space Complexity: O(n)
def prefix_to_postfix(prefix):
    st = []
    for c in reversed(prefix):
        if c.isalnum():
            st.append(c)
        else:
            op1 = st.pop()
            op2 = st.pop()
            st.append(op1+op2+c)
    return st[-1]
print(prefix_to_postfix("*-A/BC-/AKL"))  # ABC/-AK/L-*