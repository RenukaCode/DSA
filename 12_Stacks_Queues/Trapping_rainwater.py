#Brute Force Approach
# Time Complexity: O(n²)
# Space Complexity: O(1)
def fn(height):
    n=len(height)
    total = 0
    for i in range(n):
        maxLeft = 0
        maxRight = 0
        for j in range(i+1,n):
            if height[j]>maxLeft:
                maxLeft = height[j]
        for j in range(i+1,n):
            if height[j] > maxRight:
                maxRight = height[j]
        total += min(maxLeft, maxRight) - height[i]
    return total
print(fn([3,0,2,0,4]))  # 7
print(fn([0,1,0,2,1,0,1,3,2,1,2,1]))  # 14


def fn(height):
    maxLeft = 0
    maxRight = 0
    total = 0
    n=len(height)
    left = 0
    right = n-1
    while left < right:
        if height[left]<=height[right]:
            if height[left]>=maxLeft:
                maxLeft = height[left]
            else:
                total += maxLeft - height[left]
            left += 1
        else:
            if height[right]>=maxRight:
                maxRight = height[right]
            else:
                total += maxRight - height[right]
            right -= 1
    return total
print(fn([3,0,2,0,4]))  # 7
print(fn([0,1,0,2,1,0,1,3,2,1,2,1]))  # 14