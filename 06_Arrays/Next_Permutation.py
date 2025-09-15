from itertools import permutations
def next_permutation(nums):
    perms = sorted(set(permutations(nums)))
    idx = perms.index(tuple(nums))
    if idx + 1 < len(perms):
        return perms[idx + 1]
    else:
        return perms[0]
print(next_permutation([1, 2, 3]))
print(next_permutation([3, 2, 1]))

