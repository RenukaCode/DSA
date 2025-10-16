# Brute Force Approach
# Time Complexity:  O(N * (sum(arr[])-max(arr[])+1))
# Space Complexity: O(1)
def countStudents(books, limit):
    n = len(books)
    students = 1
    current_pages = 0
    for i in range(n):
        if current_pages + books[i] <= limit:
            current_pages += books[i]
        else:
            students += 1
            current_pages = books[i]
    return students
def findPages(books, n, m):
    if m > n:
        return -1
    maxi = max(books)
    sum_ = sum(books)
    for i in range(maxi, sum_ + 1):
        students_required = countStudents(books, i)
        if students_required == m:
            return i
    return maxi
print(findPages([25, 46, 28, 49, 24], 5, 4))
#  71
print(findPages([12, 34, 67, 90], 4, 2))
# 113



# Optimal Solution
# Time Complexity: O(N * log(sum(arr[])-max(arr[])+1))
# Space Complexity: O(1)
def countStudents(books, limit):
    n = len(books)
    students = 1
    current_pages = 0
    for i in range(n):
        if current_pages + books[i] <= limit:
            current_pages += books[i]
        else:
            students += 1
            current_pages = books[i]
    return students
def findPages(books, n, m):
    if m > n:
        return -1
    low = max(books)
    high = sum(books)
    while low <= high:
        mid = (low + high) // 2
        students_required = countStudents(books, mid)
        if students_required > m:
            low = mid + 1
        else:
            high = mid - 1
    return low
print(findPages([25, 46, 28, 49, 24], 5, 4))
#  71
print(findPages([12, 34, 67, 90], 4, 2))
# 113

