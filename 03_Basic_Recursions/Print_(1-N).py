#  Forward Recursion
# Time Complexity: O(N)
# Space Complexity: O(N)
def func(i, n):
    if i > n:
        return
    print(i)
    func(i + 1, n)
(func(1, 5)) 
# o/p:
    # 1
    # 2
    # 3
    # 4
    # 5


# Backward Recursion(Backtracking)
# Time Complexity: O(N)
# Space Complexity: O(N)
def func(i, n):
    if i > n:
        return
    func(i + 1, n)
    print(i)
func(1, 5)
# o/p:
    # 5
    # 4
    # 3
    # 2
    # 1

