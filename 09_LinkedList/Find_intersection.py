# Brute Force Approach
# Time Complexity: O(m*n)
# Space Complexity: O(1)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LL:
    def findIntersection(self, head1, head2):
        if not head1 or not head2:
            return None
        while head2:
            temp = head1
            while temp:
                if temp == head2:
                    return head2
                temp = temp.next
            head2 = head2.next
        return None
    def display(self, head):
        while head:
            print(head.value, end = "->")
            head = head.next
        print("None")
head = Node(3)
head.next = Node(1) 
head.next.next = Node(2)
head.next.next.next = Node(4)
head2 = head.next.next  # Node with value 2
ll = LL()
ll.display(head)                         #3->1->2->4->None
ll.display(head2)                        #2->4->None
intersection_node = ll.findIntersection(head, head2)
if intersection_node:
    print("Intersection at node with value:", intersection_node.value) 
    #Intersection at node with value: 2 



