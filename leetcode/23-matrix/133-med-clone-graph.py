import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isValid(self):
        print()

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
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

if __name__ == "__main__":
    unittest.main()
