# Brute Force Approach
# Time Complexity: O(N^2)
# Space Complexity: O(1)
def fn(arr):
    n=len(arr)
    total=0
    for i in range(n):
        smallest=arr[i]
        largest=arr[i]
        for j in range(i,n):
            smallest = min(smallest,arr[j])
            largest = max(largest,arr[j])
            total += (largest-smallest)
    return total
print(fn([1,2,3]))  #4
print(fn([1,3,3]))  #4