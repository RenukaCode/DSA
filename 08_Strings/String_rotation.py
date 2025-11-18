# Brute Force Approach
# Time Complexity: O(N^2)
# Space Complexity: O(1)
def rotation(str, goal):
    for i in range(len(str)):
        rotated = str[i:] + str[:i]
        if rotated == goal:
            return True
    return False
print(rotation("abcde", "deabc"))
# True
print(rotation("hello", "lohelx"))
# False
 
 

# Optimal Approach
# Time Complexity: O(N)
# Space Complexity: O(N)
def rotation(str, goal):
    str2 = str + str
    return goal in str2
print(rotation("abcde", "deabc"))
# True
print(rotation("hello", "lohelx"))
# False