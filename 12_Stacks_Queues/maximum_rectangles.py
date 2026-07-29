# Time Complexity: O(N*(M+M))
# Space Complexity: O(M)
def largestRectangleArea(heights):
    heights.append(0)
    st=[]
    maxarea=0
    for i in range(len(heights)):
        while st and heights[i] < heights[st[-1]]:
            height=heights[st.pop()]
            width=i if not st else i-st[-1]-1
            maxarea=max(maxarea,height*width)
        st.append(i)
    return maxarea
def maximalRectangle(matrix):
    if not matrix: return 0
    m=len(matrix[0])
    height=[0]*m
    maxarea=0
    for row in matrix:
        for i in range(m):
            if row[i] == '1':
                height[i] += 1
            else:
                height[i]=1
        maxarea=max(maxarea,largestRectangleArea(height))
    return maxarea
print(maximalRectangle([
        ['1','0','1','0','0'],
        ['1','0','1','1','1'],
        ['1','1','1','1','1'],
        ['1','0','0','1','0']
    ]))                             # 6
print(maximalRectangle([[1]]))      # 1
 