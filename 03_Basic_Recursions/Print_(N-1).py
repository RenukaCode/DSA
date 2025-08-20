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

#  OR

# Time Complexity: O(N)
# Space Complexity: O(N)
def func(i, n):
    if i < 1:
        return
    print(i)
    func(i - 1, n)
func(5, 5)
# o/p:
    # 5
    # 4
    # 3
    # 2
    # 1

