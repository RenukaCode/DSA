# Brute Force Approach
# Time Complexity: O(N * log N)
# Space Complexity: O(1)
def fn(arr,k):
    arr.sort()
    return arr
print(fn([-5,4,1,2,-3],5))  # [-5, -3, 1, 2, 4]
print(fn([5,4,3,2,1],2))    # [1, 2]



# Optimal Approach
# Time Complexity: O(N * log K)
# Space Complexity: O(k)
import heapq
def fn(arr,k):
    heap=[]
    res=[]
    for i in range(min(k+1,len(arr))):
        heapq.heappush(heap,arr[i])
    for i in range(k+1,len(arr)):
        res.append(heapq.heappop(heap))
        heapq.heappush(heap,arr[i])
    while heap:
        res.append(heapq.heappop(heap))
    return res
print(fn([6, 5, 3, 2, 8, 10, 9],3)) #[2, 3, 5, 6, 8, 9, 10]
print(fn([1, 4, 5, 2, 3, 6, 7, 8, 9, 10],2)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]