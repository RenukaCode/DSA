class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def deleteNode(self, node):
        node.value = node.next.value
        node.next = node.next.next
    def display(self):
        temp = head
        while temp:
            print(temp.value, end = " ")        
            temp = temp.next
        print()
# Usage
head = Node(4)  
head.next = Node(5)
head.next.next = Node(1)
head.next.next.next = Node(9)
node_to_delete = head.next      # Node with value 5 
solution = Solution()
solution.display()              # Output: 4 5 1 9
solution.deleteNode(node_to_delete)
solution.display()              # Output: 4 1 9   
