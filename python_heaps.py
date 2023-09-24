import heapq

# constructing a heap: O(n)
minHeap = [5, 1, 3, 7, 4, 2]
heapq.heapify(minHeap)

# Print the heap
print(list(minHeap), "Printing out the heap")

# Add a new value to the heap: O(log n)
heapq.heappush(minHeap, 11)

# Print the updated heap
print(list(minHeap), "Printing out the heap after adding an element")

# Remove and return the smallest element from the heap
smallest = heapq.heappop(minHeap)

# Print the smallest element and the updated heap
print("the smallest element and the updated heap: " , smallest, list(minHeap))

# Get the n smallest elements from the heap
nsmallest = heapq.nsmallest(3, minHeap)

# Print the n smallest elements
print(nsmallest, "nsmallest")

# Get the n largest elements from the heap
nlargest = heapq.nlargest(3, minHeap)

# Print the n largest elements
print(nlargest, "nlargest")


# getting top element: O(n)
minHeap[0]

# Length of the Min Heap: O(1)
len(minHeap)