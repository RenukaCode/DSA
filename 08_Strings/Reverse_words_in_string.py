# Brute Force Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse(s):
    words = s.split()
    reverseWords = words[::-1]
    return ' '.join(reverseWords)
print(reverse("Hello World from Python")) 
# Python from World Hello
print(reverse("  Leading and trailing spaces  "))
# spaces trailing and Leading



# Using stack
# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse(s):
    words = s.split()
    temp = []
    for word in words:
        temp.append(word)
    res = []
    while temp:
        res.append(temp.pop())
    return ' '.join(res)
print(reverse("Hello World from Python")) 
# Python from World Hello
print(reverse("  Leading and trailing spaces  "))
# spaces trailing and Leading



# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def reverse(s):
    i = len(s) - 1
    res = []
    while i >= 0:
        while i >= 0 and s[i] == ' ':
            i -= 1
        if i < 0:
            break
        j = i
        while i > 0 and s[i] != 0:
            i -= 1
        word = s[i+1:j+1]
        if len(word) == 0:
            res = word
        else:
            res += ' ' + word
    return res
print(reverse("Hello World from Python")) 
# Python from World Hello   
print(reverse("  Leading and trailing spaces  "))
# spaces trailing and Leading
        