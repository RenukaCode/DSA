# Brute Force Approach
# Time Complexity: O(N+N/2) 
# Space Complexity:  O(N/2 + N/2)
def rearrangeElements(A, n):
    pos = []
    neg = []
    for i in range(n):
        if A[i] > 0:
            pos.append(A[i])
        else:
            neg.append(A[i])
    for i in range(len(pos)):
            A[2*i] = pos[i]
    for i in range(len(neg)):
            A[2*i + 1] = neg[i]
    return A
print(rearrangeElements([1,2,-4,-5], 4))
# ouptut: [1, -4, 2, -5]
print(rearrangeElements([1,2,-3,-1,-2,3], 6))
# output: [1, -3, 2, -1, 3, -2]



# Optimal Solution
# Time Complexity: O(N)
# Space Complexity: O(1)
def rearrangeElements(nums, n):
     ans = [0] * n
     posIndex = 0
     negIndex = 1
     for i in range(n):
          if nums[i] > 0:
               ans[posIndex] = nums[i]
               posIndex += 2
          else:
               ans[negIndex] = nums[i]
               negIndex += 2
     return ans
print(rearrangeElements([1,2,-4,-5], 4))
# ouptut: [1, -4, 2, -5]
print(rearrangeElements([1,2,-3,-1,-2,3], 6))
# output: [1, -3, 2, -1, 3, -2]
               




        
              
     