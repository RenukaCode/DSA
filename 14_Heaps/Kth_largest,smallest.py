# Time Complexity: O(N * log K)
# Space Complexity: O(k)
def fn(nums,k):
    import heapq
    pq=[]
    for i in range(k):
        heapq.heappush(pq,nums[i])
    for i in range(k,len(nums)):
        if nums[i]>pq[0]:
            heapq.heappop(pq)
            heapq.heappush(pq,nums[i])
    return pq[0]
print(fn([-5,4,1,2,-3],5))  # -5
print(fn([1,2,3,4,5],2))    # 4