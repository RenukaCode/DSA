# Time Complexity: O(n)
# Space Complexity: O(n)
intMin = -2**31
intMax = 2**31
def helper(s,i,num,sign):
    if i >= len(s) or not s[i].isdigit():
        return sign*num
    num = num*10+int(s[i])
    if sign*num <= intMin: return intMin
    if sign*num >= intMax: return intMax
    return helper(s,i+1,num,sign)
def atoi(s):
    i=0
    while i <= len(s) and s[i] == ' ':
        i += 1
    sign = 1
    if i < len(s) and s[i] == '+' or s[i] == '-':
        sign = -1 if s[i] == '-' else 1
        i += 1
    return helper(s,i,0,sign)
print(atoi("-12345"))                        # -12345
