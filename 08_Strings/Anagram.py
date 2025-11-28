# Brute Force Approach
# Time Complexity: O(N Log N)
# Space Complexity: O(1)
def anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)
print(anagram("listen", "silent"))
# True  
print(anagram("hello", "world"))
# False



# Using Counter method
# Time Complexity: O(n+m)
# Space Complexity: O(N)
from collections import Counter
def anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)
print(anagram("listen", "silent"))
# True
print(anagram("hello", "world"))
# False



# Optimal Solution
# Using Dictionary
# Time Complexity: O(N)
# Space Complexity: O(N)
def anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    freq = {}
    for char in str1:
        freq[char] = freq.get(char, 0) + 1
    for char in str2:
        if char not in freq:
            return False
        freq[char] -= 1
        if freq[char] < 0:
            return False
    return True
print(anagram("listen", "silent"))
# True
print(anagram("hello", "world"))
# False



# Optimal Solution
# Time Complexity: O(N)
# Sapce Complexity: O(1)
def anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    freq = [0] * 26
    for char in str1:
        freq[ord(char) - ord('a')] += 1
    for char in str2:
        freq[ord(char) - ord('a')] -= 1
    for count in freq:
        if count != 0:
            return False
    return True
print(anagram("listen", "silent"))
# True
print(anagram("hello", "world"))
# False
