class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Sol:
    def mergeKLists(self,lists):
        if not lists:
            return None
        while len(lists)>1:
            temp=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1<len(lists) else None
                temp.append(self.mergelists(l1,l2))
            lists=temp
        return lists[0]
    def mergelists(self,l1,l2):
        dummy=ListNode(0)
        temp=dummy
        while l1 and l2:
            if l1.val>l2.val:
                dummy.next=l2
                l2=l2.next
            else:
                dummy.next=l1
                l1=l1.next
            dummy=dummy.next
        if l1:
            dummy.next=l1
        if l2:
            dummy.next=l2
        return temp.next
print(Sol().mergeKLists([ListNode(1,ListNode(4,ListNode(5))),ListNode(1,ListNode(3,ListNode(4))),ListNode(2,ListNode(6))]))  # [1,1,2,3,4,4,5,6]