import unittest
from collections import Counter
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def list_to_binary_tree(self, lst: List[Optional[int]]) -> Optional[TreeNode]:
        if not lst:
            return None
        root = TreeNode(lst[0])
        queue = [root]
        i = 1
        while queue and i < len(lst):
            node = queue.pop(0)
            if i < len(lst) and lst[i] is not None:
                node.left = TreeNode(lst[i])
                queue.append(node.left)
            i += 1
            if i < len(lst) and lst[i] is not None:
                node.right = TreeNode(lst[i])
                queue.append(node.right)
            i += 1
        return root

    def binary_tree_to_list(self, root: Optional[TreeNode]) -> List[Optional[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result

    def test_minTime_example1(self):
        n = 7
        edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
        hasApple = [False, False, True, False, True, True, False]
        expected = 8
        result = self.solution.minTime(n, edges, hasApple)
        self.assertEqual(result, expected)

    def test_minTime_example2(self):
        n = 7
        edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
        hasApple = [False, False, True, False, False, True, False]
        expected = 6
        result = self.solution.minTime(n, edges, hasApple)
        self.assertEqual(result, expected)

    def test_minTime_example3(self):
        n = 7
        edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
        hasApple = [False, False, False, False, False, False, False]
        expected = 0
        result = self.solution.minTime(n, edges, hasApple)
        self.assertEqual(result, expected)

    def test_minTime_custom(self):
        n = 7
        edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
        hasApple = [False, False, True, False, True, True, False]
        expected = 8
        result = self.solution.minTime(n, edges, hasApple)
        self.assertEqual(result, expected)


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {i: [] for i in range(n)}
        for p, c in edges:
            adj[p].append(c)
            adj[c].append(p)

        def dfs(child, parent):
            time = 0
            for c in adj[child]:
                if c == parent:
                    continue
                childTime = dfs(c, child)
                if childTime or hasApple[c]:
                    time += 2 + childTime
            return time

        return dfs(0, -1)


if __name__ == "__main__":
    unittest.main()
