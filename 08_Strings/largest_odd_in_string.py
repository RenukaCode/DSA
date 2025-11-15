# Time Complexity: O(n)
# Space Complexity: O(1)
def largest(s):
    idx = -1
    n = len(s)
    for i in range(n-1, -1, -1):
        if (int(s[i]) % 2) == 1:
            idx = i
            break
    i = 0
    while i <= idx and s[i] == '0':
        i += 1
    return s[i : idx + 1]
print(largest("503"))
# 503
print(largest("00009"))
# 9