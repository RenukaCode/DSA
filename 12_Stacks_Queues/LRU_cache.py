# Time Complexity: O(1) for get and put operations
# Space Complexity: O(capacity) for storing the cache items
class LRUCache:
    class Node:
        def __init__(self,key,val):
            self.key=key
            self.val=val
            self.next=None
            self.prev=None
    def __init__(self,capacity):
        self.head=self.Node(-1,-1)
        self.tail=self.Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.cap=capacity
        self.m={}
    def addNode(self,newnode):
        temp=self.head.next
        newnode.next=temp
        newnode.prev=self.head
        self.head.next=newnode
        temp.prev=newnode
    def deleteNode(self,delNode):
        delPrev=delNode.prev
        delNext=delNode.next
        delPrev.next=delNext
        delNext.prev=delPrev
    def get(self,key):
        if key in self.m:
            resNode=self.m[key]
            res=resNode.val
            del self.m[key]
            self.deleteNode(resNode)
            self.addNode(resNode)
            self.m[key]=self.head.next
            return res
        return -1
    def put(self,key,val):
        if key in self.m:
            existingNode=self.m[key]
            self.deleteNode(existingNode)
            del self.m[key]
        if len(self.m)==self.cap:
            del self.m[self.tail.prev.key]
            self.deleteNode(self.tail.prev)
        newNode=self.Node(key,val)
        self.addNode(newNode)
        self.m[key]=self.head.next

# Driver code
if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))   
    # 1 -1 -1 3 4