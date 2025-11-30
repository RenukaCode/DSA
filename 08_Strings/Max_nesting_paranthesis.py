# Time Complexity: O(n)
# Space Complexity: O(1)
def fn(s):
    maxi = 0
    cnt = 0
    for char in s:
        if char == '(':
            cnt += 1
        elif char == ')':
            cnt -= 1
        maxi = max(maxi, cnt)
    return maxi
print(fn("(1+(2*3)+((8)/4))+1"))
# 3
print(fn("(1)+((2))+(((3)))"))
# 3