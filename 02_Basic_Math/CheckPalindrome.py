# link: https://leetcode.com/problems/palindrome-number/

# time complexity: O(log x)
# space complexity: O(log x)
# String method Approach
def isPalindrome(x):
        dup = x
        rev = int(str(abs(x))[::-1])
        if rev == dup:
           return True
        else: 
            return False
print(isPalindrome(121))
print(isPalindrome(-121))


# time complexity: O(log x)
# space complexity: O(1)
# Math based Approach
def isPalindrome(x) -> bool:
        rev = 0
        dup = x
        while x > 0:
            lastDigit = x % 10
            rev = (rev * 10) + lastDigit
            x = x // 10
        if rev == dup:
            return True
        else:
            return False
print(isPalindrome(565656))
print(isPalindrome(3003))
print(isPalindrome(-121))

