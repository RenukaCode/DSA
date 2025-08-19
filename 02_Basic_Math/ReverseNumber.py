# link :https://leetcode.com/problems/reverse-integer/
# time complexity: O(log x)
#  space complexity: O(log x)

# String reversal approach
def reverse(x) -> int:
        sign = -1 if x < 0 else 1
        rev = int(str(abs(x))[::-1])
        if rev > (2**31) - 1:
            return 0
        return sign * rev
print(reverse(-986)) # -689
print(reverse(23000)) # 32



# time complexity: O(log x)
#  space complexity: O(log x)

# Math based reversal approach
def reverse(x) -> int:
        sign = -1 if x < 0 else 1
        rev = 0
        x = abs(x)
        while x > 0:
            lastDigit = x % 10
            rev = (rev * 10) + lastDigit
            x = x // 10
        if rev > (2**31) - 1:
            return 0
        return sign * rev
print(reverse(-987)) # -789
print(reverse(4020)) # 204
print(reverse(0)) # 0


