# Brute Force Approach
# Time Complexity: O(N^3 * log(no. of unique triplets))
# Space Complexity: O(2 * no. of the unique triplets)
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
    ans = list(st)               
    return ans
print(triplet([-1,0,1,2,-1,-4], 6))
# [[-1, 0, 1], [-1, -1, 2]]



# Better Approach
# Time Complexity:  O(NlogN)+O(N2)
# Space Complexity: O(no. of quadruplets)
def triplet(arr, n):
    st = set()
    for i in range(n):
        hashset = set()
        for j in range(i + 1, n):
            third = -(arr[i] + arr[j])
            if third in hashset:
                temp = [arr[i], arr[j], third]
                temp.sort()
                st.add(tuple(temp))
            hashset.add(arr[j])
    ans = list(st)
    return ans
print(triplet([-1,0,1,2,-1,-4], 6))
# [[-1, 0, 1], [-1, -1, 2]]



# Optimal Approach


def triplet(arr, n):
    ans = []
    arr.sort()
    for i in range(n):
        if i != 0 and arr[i] == arr[i - 1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            temp = arr[i] + arr[left] + arr[right]
            if temp < 0:
                left += 1
            elif temp > 0:
                right -= 1
            else:
                res = [arr[i], arr[left], arr[right]]
                ans.append(res)
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
    return ans
print(triplet([-1,0,1,2,-1,-4], 6))
# [[-1, 0, 1], [-1, -1, 2]]
