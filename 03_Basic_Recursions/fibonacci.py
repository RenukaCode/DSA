# Time Complexity: O(N)
# Space COmplexity: O(N)
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
# example
for i in range(10):
    print(fibonacci(i), end = " ")
# 0 1 1 2 3 5 8 13 21 34
    