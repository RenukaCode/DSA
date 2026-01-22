# Time Complexity: O(n)
# Space Complexity: O(n)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.random = None
class LL:
    def clonell(self,head):
        if not head:
            return None
        mp = {}
        temp = head
        while temp:
            mp[temp] = Node(temp.value)
            temp = temp.next
        temp = head
        while temp:
            mp[temp].next = mp.get(temp.next)
            mp[temp].random = mp.get(temp.random)
            temp = temp.next
        return mp[head]
    """
    def display(self, head):
        while head:
            rand = head.random.value if head.random else None
            print(f"({head.value},{rand})", end = "->")
            head = head.next
        print("None")"""
"""head = Node(7)
head.next = Node(14)
head.next.next = Node(21)
head.next.next.next = Node(28)

head.random = head.next.next
head.next.random = head
head.next.next.random = head.next.next.next
head.next.next.next.random = head.next
ll = LL()
ll.display(head)                  #(7,21)->(14,7)->(21,28)->(28,14)->None
cloned = ll.clonell(head)
ll.display(cloned)                #(7,21)->(14,7)->(21,28)->(28,14)->None

"""