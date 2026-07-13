# Time Complexity: O(n)
# Space Complexity: O(n)
def isValid(s):
    st = []
    for ch in s:
        if ch in '({[':
            st.append(ch)
        else:
            if not st:
                return False
            top = st.pop()
            if(ch==')' and top=='(') or (ch=='}' and top=='{') or (ch==']' and top=='['):
                continue
            else:
                return False
    return not st
print(isValid("()[{}()]")) #True
print(isValid("[( )")) #False
