def pattern1(n):
    for i in range(1, n):
        for j in range(1, n):
            print("*", end = ' ')
        print()
pattern1(5)
  # o/p: 
    # * * * * *
    # * * * * *
    # * * * * *
    # * * * * *
    # * * * * *


def pattern2(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end = " ")
        print()
pattern2(5)
  # o/p:
    # * 
    # * *
    # * * *
    # * * * * 
    # * * * * *


def pattern3(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end = " ")
        print()
pattern3(5)
  # o/p: 
    # 1
    # 1 2
    # 1 2 3
    # 1 2 3 4
    # 1 2 3 4 5


def pattern4(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end = " ")
        print()
pattern4(5)
  # o/p:  
    # 1
    # 2 2
    # 3 3 3
    # 4 4 4 4
    # 5 5 5 5 5


def pattern5(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print("*", end = " ")
        print()
pattern5(5)
  # o/p:  
    # * * * * *
    # * * * *
    # * * *
    # * *
    # *


def pattern6(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end = " ")
        print()
pattern6(5)
  # o/p:  
    # 5 4 3 2 1
    # 4 3 2 1
    # 3 2 1
    # 2 1
    # 1


def pattern7(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end = " ")
        for j in range(2 * i - 1):
            print("*", end = " ")
        for j in range(n - i):
            print(" ", end = " ")
        print()
pattern7(5)
# o/p:
    #         *         
    #       * * *   
    #     * * * * *
    #   * * * * * * *
    # * * * * * * * * *


def pattern8(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(" ", end = " ")
        for j in range(2 * i - 1):
            print("*", end = " ")
        for j in range(n - i):
            print(" ", end = " ")
        print()
pattern8(5)
# o/p:
    # * * * * * * * * *
    #   * * * * * * *
    #     * * * * *
    #       * * *
    #         *


def pattern9(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end = " ")
        for j in range(2 * i - 1):
            print("*", end = " ")
        print()
    for i in range(n - 1, 0, -1):
        for j in range(n - i):
            print(" ", end = " ")
        for j in range(2 * i - 1):
            print("*", end = " ")
            
        print()
pattern9(5)
# o/p:
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *


def pattern10(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end = " ")
        print()
    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print("*", end = " ")
        print()
pattern10(5)
  # o/p:
    # *
    # * *
    # * * *
    # * * * *
    # * * * * *
    # * * * *
    # * * *
    # * *
    # *


def pattern11(n):
    for i in range(1, n + 1):
         start = 0
         if i % 2 == 0:
                start = 1
         else: start = 0
         for j in range(1, i + 1): 
            print(start, end = " ")
            start = 1 - start     
         print()
pattern11(5)
# o/p:
# 1
# 0 1
# 0 1 0
# 1 0 1 0
# 1 0 1 0 1


def pattern12(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end = " ")
        for j in range(2 *(n - i)):
            print(" ", end = " ")
        for j in range(i, 0, -1):
            print(j, end = " ")
        print()
       
pattern12(5)
# o/p:
# 1                 1
# 1 2             2 1
# 1 2 3         3 2 1
# 1 2 3 4     4 3 2 1
# 1 2 3 4 5 5 4 3 2 1


def pattern13(n):
    nums = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(nums, end = " ")
            nums += 1
        print()
pattern13(5)
# o/p:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
            

def pattern14(n):
    for i  in range(1, n + 1):
        for j in range(1, i + 1):
            print(chr(65 + j - 1), end = " ")
        print()
pattern14(5)
# o/p:
# A
# A B
# A B C
# A B C D
# A B C D E


def pattern15(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(chr(65 + j - 1), end = " ")
        print()
pattern15(5)
# o/p:
# A B C D E
# A B C D
# A B C
# A B
# A


def pattern16(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(chr(65 + i - 1), end = " ")
        print()
pattern16(5)
# o/p:
# A
# B B
# C C C
# D D D D
# E E E E E

# def pattern*(n):
#     for i in range(n):
#         for k in range(n - i):
#             print(" ", end = " ")
#         for j in range(i):
#             print("*", end = " ")
#         print(end = '\n')
# pattern*(5)