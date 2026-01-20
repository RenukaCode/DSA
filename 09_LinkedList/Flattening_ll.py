# Brute Force Approach
# Time Complexity: O(N x M) + O(N x M log(N x M)) + O(N x M)
# Space Complexity:  O(N x M) + O(N x M)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.child = None
class LL:
    def convert(self, arr):
        dummy = Node(-1)
        temp = dummy
        for i in range(len(arr)):
            temp.child = Node(arr[i])
            temp = temp.child
        return dummy.child
    def flatten(self, head):
        if not head:
            return 
        arr = []
        while head is not None:
            t2 = head
            while t2 is not None:
                arr.append(t2.value)
                t2 = t2.child
            head = head.next
        arr.sort()
        return self.convert(arr)
    """
    def displayNext(self, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")
    def displayChild(self, head):
        while head:
            print(head.value, end = "->")
            head = head.child
        print("None")"""
"""
head = Node(5)
head.child = Node(14)

head.next = Node(10)
head.next.child = Node(4)

head.next.next = Node(12)
head.next.next.child = Node(20)
head.next.next.child.child = Node(13)

head.next.next.next = Node(7)
head.next.next.next.child = Node(17)
ll = LL()
ll.displayNext(head)                   #5 -> 10 -> 12 -> 7 -> None
flattened = ll.flatten(head)
ll.displayChild(flattened)             #4 -> 5 -> 7 -> 10 -> 12 -> 13 -> 14 -> 17 -> 20 -> None
"""



# Optimal Solution
# Time Complexity: O(N x (2M)) ~ O(2N x M)
# Space Complexity: O(1)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.child = None
class LL:
    def merge(self,list1,list2):
        dummy = Node(-1)
        res = dummy
        while list1 is not None and list2 is not None:
            if list1.value < list2.value:
                res.child = list1
                res = list1
                list1 = list1.child
            else:
                res.child = list2
                res = list2
                list2 = list2.child
            res.next = None
        if list1:
            res.child = list1
        else:
            res.child = list2
        if dummy.child:
            dummy.child.next = None
        return dummy.child
    def flatten(self,head):
        if head is None or head.next is None:
            return head
        mergedhead = self.flatten(head.next)
        head = self.merge(head,mergedhead)
        return head
    """
    def displayNext(seld, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")
    def displayChild(seld, head):
        while head:
            print(head.value, end = "->")
            head = head.child
        print("None")"""
"""
head = Node(5)
head.child = Node(14)

head.next = Node(10)
head.next.child = Node(4)

head.next.next = Node(12)
head.next.next.child = Node(20)
head.next.next.child.child = Node(13)

head.next.next.next = Node(7)
head.next.next.next.child = Node(17)
ll = LL()
ll.displayNext(head)                   #5 -> 10 -> 12 -> 7 -> None
flattened = ll.flatten(head)
ll.displayChild(flattened)             #4 -> 5 -> 7 -> 10 -> 12 -> 13 -> 14 -> 17 -> 20 -> None"""