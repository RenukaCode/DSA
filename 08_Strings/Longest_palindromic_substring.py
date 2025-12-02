# Time Complexity: O(n^2)
# Space Complexity: O(1)
def fn(s):
    n = len(s)
    res = ''
    for i in range(n):
        # even
        l = i
        r = i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            cur = s[l:r+1]
            if len(cur) > len(res):
                res = cur
            r += 1
            l -= 1
        # odd
        l = i
        r = i
        while l >= 0 and r < n and s[l] == s[r]:
            cur = s[l:r+1]
            if len(cur) > len(res):
                res = cur
            r += 1
            l -= 1
    return res
print(fn("babad"))
# "bab"
print(fn("cbbd"))
# "bb"