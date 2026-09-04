
# Optimal Approach: Quickselect
# Time Complexity: O(N) on average, O(N^2) in worst case
# Space Complexity: O(1)
import random
def partition(nums,left,right):
    pvtIdx = random.randint(left,right)
    pivot = nums[pvtIdx]
    nums[pvtIdx],nums[left]=nums[left],nums[pvtIdx]
    store=left
    for i in range(left+1,right+1):
        if nums[i]<pivot:
            store+=1
            nums[i],nums[store]=nums[store],nums[i]
    nums[store],nums[left]=nums[left],nums[store]
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
print(quickselect([-5,4,1,2,-3],5))  # 4
print(quickselect([1,2,3,4,5],2))    # 2
print(quickselect([1,2,3,4,5],1))    # 1



# Time Complexity: O(N * log K)
# Space Complexity: O(k)
def fn(nums,k):
    import heapq
    pq=[]
    for i in range(k):
        heapq.heappush(pq,-nums[i])
    for i in range(k,len(nums)):
        if nums[i]<-pq[0]:
            heapq.heappop(pq)
            heapq.heappush(pq,-nums[i])
    return -pq[0]
print(fn([-5,4,1,2,-3],5))  # 4
print(fn([1,2,3,4,5],2))    # 2
print(fn([1,2,3,4,5],1))    # 1