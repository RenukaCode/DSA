# Time Complexity: O(n)
# Space Complexity: O(n)
def fn(n):
    seen,res = [0]*n,0
    for num in range(2,n):
        if seen[num]:
            continue
        res += 1
        seen[num*num:n:num] = [1]*((n-1)//num-num+1)
    return res
print(fn(10)) #4
print(fn(0)) #0
print(fn(1)) # 0