# Time Complexity: O(n)
# Space Complexity: O(n)
def fn(n):
    seen, ans = [0] * n, 0
    for num in range(2, n):
        if seen[num]: continue
        ans += 1
        seen[num*num:n:num] = [1] * ((n - 1) // num - num + 1)
    return ans
print(fn(10)) #4
print(fn(5)) #2
