# Time Complexity: O(N)
# Space Complexity: O(N)
def func(n):
    if n == 0 or n == 1:
        return 1
    return n * func(n - 1)
print(func(5)) # 120
print(func(7)) # 5040
