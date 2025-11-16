# Time Complexity: O(N *log N + M)
# Space Complexity: O(M)
def longet(str):
    if not str:
        return ""
    str.sort()
    first = str[0]
    last = str[-1]
    res = []
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            res.append(first[i])
        else:
            break
    return ''.join(res)
print(longet(["flower","flow","flight"]))
# fl
print(longet(["dog","racecar","car"]))
# ""
print(longet(["interspecies","interstellar","interstate"]))
# inters