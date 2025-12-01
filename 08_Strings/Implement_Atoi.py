# Time Complexity: O(N)
# Space Complexity: O(1)
def fn(s):
    i = 0
    sign = 1
    res = 0
    while i < len(s) and s[i] == ' ':
        i += 1
    if i == len(s):
        return 0
    if s[i] == '+':
        i += 1
    elif s[i] == '-':
        sign = -1
        i += 1
    while i < len(s) and s[i].isdigit():
        res = res * 10 + int(s[i])
        if sign * res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if sign * res < -2 ** 31:
            return -2 ** 31
        i += 1
    return sign * res
print(fn("1337c0d3"))
# 1337
print(fn("words and 987"))
# 0

    