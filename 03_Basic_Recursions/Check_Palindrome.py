# Time Complexity: O(N)
# Space COmplexity: O(N)
def isPalindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return isPalindrome(s, left + 1, right - 1)
#Example
s = "madam"
print(isPalindrome(s, 0, len(s) - 1)) 
# True
s = "hell"
print(isPalindrome(s, 0, len(s) - 1)) 
# False


# Time Complexity: o(N)
# Space COmplexity:O(N)
import re
def isPalindrome(s):
    s = re.sub('[^a-zA-Z0-9]','',s).lower()
    return s == s[::-1]
# example
s = "madam"
print(isPalindrome(s))
# True
s= "abc d cba"
print(isPalindrome(s))
# True
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s)) 
# True
