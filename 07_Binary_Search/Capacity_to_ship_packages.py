def days(weights, cap):
    n = len(weights)
    day = 1
    load = 0
    for i in range(n):
        if load + weights[i] > cap:
            day += 1
            load = weights[i]
        else:
            load += weights[i]
    return day
def leastCapacity(weights, d):
    maxi = max(weights)
    sum_ = sum(weights)
    for i in range(maxi, sum_ + 1):
        if days(weights, i) <= d:
            return i
    return -1
print(leastCapacity([5, 4, 5, 2, 3, 4, 5, 6],5))
# 9
print(leastCapacity([1,2,3,4,5,6,7,8,9,10],1))
# 55


def days(weights, cap):
    day = 1
    load = 0
    n = len(weights)
    for i in range(n):
        if load + weights[i] > cap:
            day += 1
            load = weights[i]
        else:
            load += weights[i]
    return day
def leastCapacity(weights, d):
    low = max(weights)
    high = sum(weights)
    res = -1
    while low <= high:
        mid = (low + high) // 2
        if days(weights, mid) <= d:
            res =  mid
            high = mid - 1
        else:
            low = mid + 1
    return res
print(leastCapacity([5, 4, 5, 2, 3, 4, 5, 6],5))
# 9
print(leastCapacity([1,2,3,4,5,6,7,8,9,10],1))
# 55


def shipWithindays(weights, days):
    low = max(weights)
    high = sum(weights)
    while low <= high:
        mid, day, load = (low + high) // 2, 1, 0
        for w in weights:
            if load + w > mid:
                day += 1
                load = 0
            else:
                load += w
        if day > days: low = mid + 1
        else: high = mid
    return low
print(leastCapacity([5, 4, 5, 2, 3, 4, 5, 6],5))
# 9
print(leastCapacity([1,2,3,4,5,6,7,8,9,10],1))
# 55