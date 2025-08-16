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
    for i in range(1, n + 1):
        for j in range(1, n - i + 2):
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
    for i in range(1, n + 1):
        for j in range(1, n - i + 2):
            print(j, end = " ")
        print()
pattern6(5)
    # o/p:  
    # 0 1 2 3 4
    # 0 1 2 3
    # 0 1 2
    # 0 1
    # 0






