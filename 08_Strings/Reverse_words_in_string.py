# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse(s):
    words = s.split()
    reverseWords = words[::-1]
    return ' '.join(reverseWords)
print(reverse("Hello World from Python")) 

