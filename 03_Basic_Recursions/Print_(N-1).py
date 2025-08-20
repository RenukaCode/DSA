def func(i, n):
    if i > n:
        return
    func(i + 1, n)
    print(i)
func(1, 5)

#  OR

def func(i, n):
    if i < 1:
        return
    print(i)
    func(i - 1, n)
func(5, 5)

# Time Complexity: O(N)
# Space Complexity: O(N)