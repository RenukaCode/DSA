# By Recursion
# TIme Complexity: O(N)
# Space Complexity: O(N)
def func(n):
    if n == 0:
        return 0
    return n + func(n - 1)
print(func(5)) 

# Without Recursion
# TIme Complexity: O(1)
# Space Complexity: O(1)
def func(n):
    sum = int(n *(n + 1)/2)
    print(sum)
func(5) # 15
func(20) # 210

