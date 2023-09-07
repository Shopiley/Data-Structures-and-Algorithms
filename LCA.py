def hasCommonAncestor(pairs, nodeA, nodeB):
    # create adjacency list - dictionary of child to parent key-value pairs
    adj_list = {}
    for pair in pairs:
        parent, child = pair
       
        if child not in adj_list:
            adj_list[child] = []
           
        if parent not in adj_list:
            adj_list[parent] = []

        adj_list[child].append(parent)

    print(adj_list)

    # perform dfs on both nodeA and nodeB to get a array of all their ancestors
    ancestorsA = dfs(adj_list, nodeA)
    ancestorsB = dfs(adj_list, nodeB)
    m = len(ancestorsA)
    n = len(ancestorsB)
   
    # check for common element between the two arrays
    if m <= n:
        for i in range(m):
            if ancestorsA[i] in ancestorsB:
                return True
    else:
        for i in range(n):
            if ancestorsB[i] in ancestorsA:
                return True
    return False

# function performs dfs on a node and returns a array of their ancestors (direct or indirect)
def dfs(adj_list, node):
    stack = [node] #[]
    ancestors = [] #[4, 14]

    while stack:
        current = stack.pop()
        for neighbour in adj_list[current]:
            stack.append(neighbour)
            ancestors.append(neighbour)
    return ancestors

pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (15, 21),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9),
    (15, 13)
]

# test cases          
print(hasCommonAncestor(pairs, 3, 8))  
# print(hasCommonAncestor(pairs, 5, 8))
# print(hasCommonAncestor(pairs, 6, 8))
# print(hasCommonAncestor(pairs, 6, 9))
# print(hasCommonAncestor(pairs, 1, 3))
# print(hasCommonAncestor(pairs, 3, 1))
# print(hasCommonAncestor(pairs, 7, 11))
# print(hasCommonAncestor(pairs, 6, 5))  
# print(hasCommonAncestor(pairs, 5, 6))
