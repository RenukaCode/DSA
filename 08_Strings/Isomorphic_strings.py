# Time Complexity: O(n)
# Space Complexity: O(1)
def isomorphic(s, t):
    n = len(s)
    m1, m2 = [0] * 256, [0] * 256
    for i in range(n):
        if m1[ord(s[i])] != m2[ord(t[i])]:
            return False
        m1[ord(s[i])] = i + 1
        m2[ord(t[i])] = i + 1
    return True
print(isomorphic("egg", "add"))
# True
print(isomorphic("foo", "bar"))
# False 