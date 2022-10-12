# Deque is preferred over the list in the cases where we need 
# quicker append and pop operations from both the ends of the 
# container, as deque provides an O(1) time complexity for 
# append and pop operations as 
# compared to list which provides O(n) time complexity. 

from collections import deque       

# # ITERATIVE METHOD
# def depthFirstPrint(graph, source):
#     stack = deque()

#     stack.append(source)

#     while (len(stack) > 0):
#         current = stack.pop()
#         print(current)      #print  your node right after it leaves the stack not when it's added

#         for neighbour in graph[current]:
#             stack.append(neighbour)


#RECURSIVE METHOD
def depthFirstPrint(graph, source):
    print(source)
    for neighbour in graph[source]:
        depthFirstPrint(graph, neighbour)   # in this example, b is called first here, then it's neighbours are recursively called

# this method also uses stacks bcoz remember, stacks are the basis for reccursive calls
# in this recursive call, the base case is implicit - in the for loop because if the node at the moment has no neighbours, then the function won't be called again

graph = {
    'a': ['b', 'c'],    # in the iterative method, c is going to be printed right after a instead of b because, b is pushed in first so see will be on top
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


depthFirstPrint(graph, 'a')