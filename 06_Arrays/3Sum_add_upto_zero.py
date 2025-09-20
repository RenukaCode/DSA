def triplet(arr, n):
    st =set()
    sum = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] ==0:
                    res = [arr[i], arr[j], arr[k]]
                    res.sort()
                    st.add(tuple(res))
    ans = [list(item) for item in st]               
    return ans
print(triplet([-1,0,1,2,-1,-4], 6))
# [[-1, 0, 1], [-1, -1, 2]]
