# BruteForce Approach
# Time Complexity: O(N^N)
# Space Complexity: O(N)
def fn(arr):
    maxarea=0
    for i in range(len(arr)):
        height=float('inf')
        for j in range(i,len(arr)):
            height=min(height,arr[j])
            width=j-i+1
            area=width*height
            maxarea=max(maxarea,area)
    return maxarea
print(fn([2,1,5,6,2,3,1]))  #10



#Optimal Approach
# Time Complexity: O(2N)
# Space Complexity: O(N)
def fn(arr):
    st=[]
    maxarea=0
    n=len(arr)
    for i in range(n+1):
        curheight=arr[i] if i<n else 0
        while st and (i==n or arr[st[-1]] >= curheight):
            height=arr[st.pop()]
            if not st:
                width=i
            else:
                width=i-st[-1]-1
            maxarea=max(maxarea,height*width)
        st.append(i)
    return maxarea
print(fn([2,1,5,6,2,3,1]))  # 10
