# link: https://leetcode.com/problems/armstrong-number/description/
# time complexity: O(log10N + 1)
# space complexity: O(1)

def check_num(num):
    k = len(str(num))
    n = num
    sum = 0
    while n > 0:
        i = n % 10
        sum += i ** k
        n = n // 10
    return sum == num
print(check_num(371)) # true
print(check_num(153)) # true
print(check_num(123)) # false
