import unittest
from collections import deque

def get_path(graph, start_node, end_node):
    
    if start_node not in graph or end_node not in graph:
        raise Exception

    # Find the shortest route in the network between the two users
    queue = deque(start_node)
    how_we_reached = {start_node: None}
    
    while queue: # O(n)
        current = queue.popleft()
        
        if current == end_node:
            # this takes function O(n) too but at the point in which it is called, the outer while loop ends
            print (start_node, "->", end_node, "=", reconstruct_path(how_we_reached, start_node, end_node))
            return reconstruct_path(how_we_reached, start_node, end_node)
        
        for neighbour in graph[current]:
            if neighbour not in how_we_reached:
                queue.append(neighbour)
                how_we_reached[neighbour] = current
                

    return None



def reconstruct_path(how_we_reached, start_node, end_node):
    # backtracking to assemble the path we used to reach our end_node.
    path = []
    
    current = end_node

    while current:
        path.append(current)
        current = how_we_reached[current]
        
    path.reverse()
    return path
        

"""
Time complexity: O(n + m) where n is the number of node and m, the number of edges
Space Complexity: O(n)
"""


# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'a', 'h')


unittest.main(verbosity=2)