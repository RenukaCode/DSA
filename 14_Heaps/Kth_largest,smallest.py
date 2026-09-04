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



# Optimal Approach: Quickselect
# Time Complexity: O(N) on average, O(N^2) in worst case
# Space Complexity: O(1)
import random
def partition(nums,left,right):
    pvtIdx = random.randint(left,right)
    pivot = nums[pvtIdx]
    nums[pvtIdx],nums[right]=nums[right],nums[pvtIdx]
    store=left
    for i in range(left,right):
        if nums[i]>pivot:
            nums[i],nums[store]=nums[store],nums[i]
            store+=1
    nums[store],nums[right]=nums[right],nums[store]
    return store
def quickselect(nums,k):
    left,right=0,len(nums)-1
    while True:
        pvtIdx=partition(nums,left,right)
        if pvtIdx==k-1:
            return nums[pvtIdx]
        elif pvtIdx>k-1:
            right=pvtIdx-1
        else:
            left=pvtIdx+1
print(quickselect([-5,4,1,2,-3],5))  # -5
print(quickselect([1,2,3,4,5],2))    # 4
print(quickselect([1,2,3,4,5],1))    # 5