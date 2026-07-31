# Brute Force Approach
# Time Complexity: O(N²)
# Space Complexity: O(n)
def fn(M):
    n=len(M)
    knowMe=[0]*n
    IKnow=[0]*n
    for i in range(n):
        for j in range(n):
            if M[i][j]==1:
                knowMe[j]+=1
                IKnow[i]+=1
    for i in range(n):
        if knowMe[i] == n-1 and IKnow[i] == 0:
            return i
    return -1
print(fn( [
        [0, 1, 1, 0], 
        [0, 0, 0, 0], 
        [1, 1, 0, 0], 
        [0, 1, 1, 0]
    ]))                           # 1
print(fn([ [0, 1], [1, 0] ]))     # -1



# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def fn(M):
    n=len(M)
    top, down = 0,n-1
    while top < down:
        if M[top][down] == 1:
            top += 1
        elif M[down][top] == 1:
            down -= 1
        else:
            top += 1
            down -= 1
    if top > down:
        return -1
    for i in range(n):
        if i == top:
            continue
        if M[top][i] == 1 or M[i][top] == 0:
            return -1
    return top
print(fn( [
        [0, 1, 1, 0], 
        [0, 0, 0, 0], 
        [1, 1, 0, 0], 
        [0, 1, 1, 0]
    ]))                           # 1
print(fn([ [0, 1], [1, 0] ]))     # -1
