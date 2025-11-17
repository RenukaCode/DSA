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



# Time Complexity: O(n)
# Space Complexity: O(n)
def isomorphic(s, t):
    s_idx = {}
    t_idx = {}
    for i in range(len(s)):
        if s[i] not in s_idx:
            s_idx[s[i]] = i
        if t[i] not in t_idx:
            t_idx[t[i]] = i
        if s_idx[s[i]] != t_idx[t[i]]:
            return False
    return True
print(isomorphic("paper", "title"))
# True
print(isomorphic("egg", "add"))
# True
print(isomorphic("foo", "bar"))
# False 