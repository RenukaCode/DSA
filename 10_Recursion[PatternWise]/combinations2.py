# Time Complexity :  O(2n * k)
# Space Complexity: O(k * x)
def fn(idx, target, arr, ans, ds):
    if target == 0:
        ans.append(list(ds))
        return
    for i in range(idx, len(arr)):
        if i > idx and arr[i] == arr[i-1]:
            continue
        if arr[i] > target:
            break
        ds.append(arr[i])
        fn(i+1, target - arr[i], arr, ans, ds)
        ds.pop()
def combinations2(candidates, target):
    candidates.sort()
    ans = []
    ds = []
    fn(0, target, candidates, ans, ds)
    return ans
# candidates = [10,1,2,7,6,1,5]
# target = 8
# print(combinations2(candidates, target))
# # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
