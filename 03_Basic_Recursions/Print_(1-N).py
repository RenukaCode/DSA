#  Forward Recursion
def func(i, n):
    if i > n:
        return
    print(i)
    func(i + 1, n)
(func(1, 5))

# Backward Recursion(Backtracking)
def func(i, n):
    if i > n:
        return
    func(i + 1, n)
    print(i)
func(1, 5)

# Time Complexity: O(N)
# Space Complexity: O(N)