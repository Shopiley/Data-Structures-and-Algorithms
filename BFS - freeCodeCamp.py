from collections import deque

def breadthFirstPrint(graph, source):
    queue = deque([source])
    traversal = []
    
    while (len(queue) > 0):   #while queue is not empty
        current = queue.popleft()
        traversal.append(current)

        for neighbour in graph[current]: 
            queue.append(neighbour)

    return traversal
graph = {
    'a': ['b', 'c'],  
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}   
print(breadthFirstPrint(graph, 'a'))

