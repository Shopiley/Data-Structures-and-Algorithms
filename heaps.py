"""
implementing a min-heap
inserting to a heap: O(log n)
deleting top from a heap: O(log n)
retriving the top element: O(1)
"""
class MinHeap():

    items = []
    size = 0

    def getLeftChildIndex(self, parentIndex):
        return 2 * parentIndex + 1

    def getRightChildIndex(self, parentIndex):
        return 2 * parentIndex + 2
    
    def getParentIndex(self, childIndex):
        return (childIndex - 1)//2
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def leftChild(self, index):
        return self.items[self.getLeftChildIndex(index)]
    
    def rightChild(self, index):
        return self.items[self.getRightChildIndex(index)]
    
    def parent(self, index):
        return self.items[self.getParentIndex(index)]
    
    def swap(self, indexOne, indexTwo):
        self.items[indexOne], self.items[indexTwo] = self.items[indexTwo], self.items[indexOne]

    def peek(self):
        print("\nprinting min value...")
        if self.size == 0:
            raise RuntimeError
        print (self.items[0])
    
    def extract_min(self):      # O(log n)
        print("\nextracting min...")
        if self.size == 0:
            raise RuntimeError
        item = self.items[0]
        self.items[0] = self.items.pop()
        self.size -= 1
        self.HeapifyDown()
        print (item)
    
    def insert(self, item):     # O(log n)
        print(f"\ninserting {item}...")
        self.items.append(item)
        self.size += 1
        print("attempting to heapifyUp...")
        self.HeapifyUp()

    def HeapifyUp(self):
        index = self.size - 1
        while (self.hasParent(index) and self.parent(index) > self.items[index]):
                print("Carrying out heapifyUp()...")
                self.swap(self.getParentIndex(index), index)
                index = self.getParentIndex(index) 
        print("end of heapify up")

    def HeapifyDown(self):
        index = 0
        while (self.hasLeftChild(index)):      #there can't be a right child without a left child
            print("Carrying out heapifyDown()...")
            smallerChildIndex = self.getLeftChildIndex(index)
            if (self.hasRightChild(index) and self.leftChild(index) > self.rightChild(index)):
                smallerChildIndex = self.getRightChildIndex(index)           
            if (self.items[index] < smallerChildIndex):
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex 
        print("end of heapify down")


    
myHeap = MinHeap()
print("state of the heap: ", myHeap.items)
myHeap.insert(4)
print("state of the heap: ", myHeap.items)
myHeap.insert(9)
print("state of the heap: ", myHeap.items)
myHeap.insert(3)
print("state of the heap: ", myHeap.items)
myHeap.insert(1)
print("state of the heap: ", myHeap.items)
myHeap.peek()
print("state of the heap: ", myHeap.items)
myHeap.extract_min()
print("state of the heap: ", myHeap.items)
myHeap.peek()
print("state of the heap: ", myHeap.items)
