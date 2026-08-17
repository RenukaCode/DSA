# Heap is a binary tree used to implement priority queues. It's structured to always keep the highest priority.
# Min heap -> Each parent node is smaller than its children.
# Max heap -> Each parent node is greater than its children.

# Root at arr[0]
# left child of node at idx i -> 2*i+1
# right child of node at idx i -> 2*i+2
# parent node at idx i -> (i-1)/2

# Operations with Min heap
#     1. Insert() -> inserts new key.
#     2. Heapify() -> Used to restore Minheap, by fixing violation.
#     3. getMin()  -> returns minimum value.
#     4. ExtractMin() -> removes minimum element.
#     5. Delete()  -> delete value at that idx .
#     6. Decreasekey() -> update value at idx with given value.



# IMPLEMENTATION
class BinaryHeap:
    def __init__(self,capacity):
        self.capacity=capacity
        self.size=0
        self.arr=[0]*capacity
    def parent(self,i):
        return (i-1)//2
    def left(self,i):
        return 2*i+1
    def right(self,i):
        return 2*i+2
    
    # Insert a new key into the heap
    def insert(self,x):
        if self.size==self.capacity:
            print("Binary Heap overflow")
            return
        self.arr[self.size]=x    # Place new element at the end
        k=self.size              # index of inserted element
        self.size+=1

        # Bubble up to fix min-heap property
        while k!=0 and self.arr[self.parent(k)] > self.arr[k]:
            self.arr[self.parent(k)], self.arr[k] = self.arr[k], self.arr[self.parent(k)]
            k=self.parent(k)

    # Heapify function (fix min-heap property starting at index idx)
    def heapify(self,idx):
        li=self.left(idx)
        ri=self.right(idx)
        smallest=idx
        # Check if left child is smaller
        if li<self.size and self.arr[li]<self.arr[smallest]:
            smallest = li
        # Check if right child is smaller
        if ri < self.size and self.arr[ri] < self.arr[smallest]:
            smallest = ri
        # If parent is not smallest, swap and recurse
        if smallest != idx:
            self.arr[idx], self.arr[smallest] = self.arr[smallest], self.arr[idx]
            self.heapify(smallest)

    # Return the minimum element (root of heap)
    def get_min(self):
        if self.size==0:
            return float('-inf')
        return self.arr[0]

    # Extract minimum element and fix heap
    def extract_min(self):
        if self.size == 0:
            return float("-inf")
        if self.size==1:
            self.size-=1
            return self.arr[0]
        # Store minimum value
        mini=self.arr[0]
        # Move last element to root
        self.arr[0] = self.arr[self.size-1]
        self.size-=1
        # Call heapify on root
        self.heapify(0)
        return mini

    # Decrease key value at index i to val
    def decrease_key(self,i,val):
        self.arr[i]=val   # update value
        # Bubble up until heap property is satisfied
        while i != 0 and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[self.parent(i)], self.arr[i] = self.arr[i],self.arr[self.parent(i)]
            i=self.parent(i)

    # Delete element at index i
    def delete(self,i):
        # First decrease its value to -infinity
        self.decrease_key(i,float("-inf"))
        # Then extract minimum (which removes it)
        self.extract_min()

    # Print heap elements
    def print_heap(self):
        for i in range(self.size):
            print(self.arr[i], end=" ")
        print()

# Driver code to test
if __name__ == "__main__":
    h = BinaryHeap(20)
    h.insert(4)
    h.insert(1)
    h.insert(2)
    h.insert(6)
    h.insert(7)
    h.insert(3)
    h.insert(8)
    h.insert(5)

    print("Min value is", h.get_min())  # should be 1
    h.insert(-1)
    print("Min value is", h.get_min())  # should be -1
    h.decrease_key(3, -2)  # update element at index 3
    print("Min value is", h.get_min())  # should be -2
    h.extract_min()
    print("Min value is", h.get_min())  # should be -1
    h.delete(0)
    print("Min value is", h.get_min())  # should be 1
