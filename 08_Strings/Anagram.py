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