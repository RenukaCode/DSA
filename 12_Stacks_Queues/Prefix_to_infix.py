# Time Complexity: O(n)
# Space Complexity: O(n)
def prefix_to_infix(prefix):
    st = []
    for c in reversed(prefix):
        if c.isalnum():
            st.append(c)
        else:
            op1 = st.pop()
            op2 = st.pop()
            st.append(f"({op1}{c}{op2})")
    return st[-1]
print(prefix_to_infix("*-A/BC-/AKL"))   # ((A-(B/C))*((A/K)-L))