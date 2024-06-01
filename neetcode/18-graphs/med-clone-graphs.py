import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_cloneGraph(self):
        nodes = [Node(i) for i in range(1, 4)]
        nodes[0].neighbors = [nodes[1]]
        nodes[1].neighbors = [nodes[0], nodes[2]]
        nodes[2].neighbors = [nodes[1]]

        result = self.solution.cloneGraph(nodes[0])
        print()
        # You need to implement a function to convert the result back to an adjacency list for comparison
        # self.assertEqual(self.convert_to_adjList(result), [[2], [1, 3], [2]])

        # # For the case of an empty graph
        # result = self.solution.cloneGraph(None)
        # # self.assertEqual(self.convert_to_adjList(result), [[]])

        # # For the case of a graph with a single node with no neighbors
        # node = Node(1)
        # result = self.solution.cloneGraph(node)
        # # self.assertEqual(self.convert_to_adjList(result), [[1]])


# def convert_to_adjList(node):
#     adjList = []
#     visited = set()

#     def dfs(node):
#         if node.val in visited:
#             return
#         visited.add(node.val)
#         neighbors = [neighbor.val for neighbor in node.neighbors]
#         adjList.append(neighbors)
#         for neighbor in node.neighbors:
#             dfs(neighbor)

#     dfs(node)
#     return adjList


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        visit = {}

        def dfs(node):
            if node in visit:
                return visit[node]
            newNode = Node(node.val)
            visit[node] = newNode
            for n in node.neighbors:
                newNode.neighbors.append(dfs(n))
            return newNode

        return dfs(node) if node else None


class NeedCodeSolution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None


if __name__ == "__main__":
    unittest.main()
