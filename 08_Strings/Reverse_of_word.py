# Brute Force Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def fn(s):
    n = len(s)
    words = []
    start = end = 0
    i = 0
    while i < n:
        while i < n and s[i] == ' ':
            i += 1
        if i >= n:
            break
        start = i
        while i < n and s[i] != ' ':
            i += 1
        end = i - 1
        wordsFound = s[start:end+1]
        words.append(wordsFound)
    res = ''
    for i in range(len(words) -1, -1, -1):
        res += words[i]
        if i != 0:
            res += ' '
    return res
print(fn("the sky is blue"))
# "blue is sky the"
print(fn("  hello world  "))
# "world hello"



# Optimal Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
def fn(s):
    words = s.split()
    reversed = words[::-1]
    return ' '.join(reversed)
print(fn("the sky is blue"))
# "blue is sky the"
print(fn("  hello world  "))
# "world hello"