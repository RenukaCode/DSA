# Time Complexity: O(n)
# Space Complexity: O(1)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LL:
    def reverseK(self, head, k):
        dummy = Node(0)
        dummy.next = head
        grpPrev = dummy
        while True:
            kth = self.getK(grpPrev, k)
            if not kth:
                break
            grpNxt = kth.next
            prev = grpNxt
            curr = grpPrev.next
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = grpPrev.next
            grpPrev.next = kth
            grpPrev = temp
        return dummy.next
    def getK(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    def display(self, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
ll = LL()
ll.display(head)                     #1->2->3->4->5->None
new_head = ll.reverseK(head, 2)
ll.display(new_head)                 #2->1->4->3->5->None
