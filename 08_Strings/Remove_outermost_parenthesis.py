def fn(s):
    str = ""
    lvl = 0
    for char in s:
        if char == '(':
            if lvl > 0:
                str += char
            lvl += 1
        elif char == ')':
            lvl -= 1
            if lvl > 0:
                str += char
    return str
print(fn("((()))")) 
# (())
print(fn("()(()())(())")) 
# ()()()()