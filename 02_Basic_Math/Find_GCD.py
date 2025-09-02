# time complexity: O(log(min(a, b)))
# space complexity: O(N)

# Euclidian formula(gcd(a, b) = gcd(b, a % b)  (if b ≠ 0)
#                   gcd(a, 0) = a  (base case))
def find_gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        return b
    else: 
        return a
print(find_gcd(20, 15)) # 5
print(find_gcd(24, 6)) # 6
        
