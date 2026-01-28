# Time Complexity: O(2^n)
# Space Complexity: O(n)
MOD = 10**9 + 7
def goodNos(idx,n):
    if idx == n:
        return 1
    res = 0
    if idx % 2 == 0:
        evenDigits = [0,2,4,6,8]
        for digit in evenDigits:
            res = (res + goodNos(idx + 1, n)) % MOD
    else:
        primeDigits = [2,3,5,7]
        for digit in primeDigits:
            res = (res + goodNos(idx + 1, n)) % MOD
    return res
print(goodNos(0,2))          #20
print(goodNos(0,3))          #100
print(goodNos(1,1))          #1