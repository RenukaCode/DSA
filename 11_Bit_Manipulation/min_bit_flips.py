# Time Complexity: O(1)
# Space Complexity: O(1)
def fn(start,goal):
    num = start^goal
    cnt = 0
    for i in range(32):
        cnt += (num&1)
        num >>= 1
    return cnt
print(fn(10,7)) # 3
print(fn(3,4)) # 3
