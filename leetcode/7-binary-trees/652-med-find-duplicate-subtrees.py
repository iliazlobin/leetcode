import unittest
from collections import Counter, defaultdict
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

    def test_findDuplicateSubtrees_example1(self):
        root = self.list_to_binary_tree([1, 2, 3, 4, None, 2, 4, None, None, 4])
        expected = [[2, 4], [4]]
        result = self.solution.findDuplicateSubtrees(root)
        result_list = [self.binary_tree_to_list(node) for node in result]
        self.assertEqual(sorted(result_list), sorted(expected))

    def test_findDuplicateSubtrees_example2(self):
        root = self.list_to_binary_tree([2, 1, 1])
        expected = [[1]]
        result = self.solution.findDuplicateSubtrees(root)
        result_list = [self.binary_tree_to_list(node) for node in result]
        self.assertEqual(sorted(result_list), sorted(expected))

    def test_findDuplicateSubtrees_example3(self):
        root = self.list_to_binary_tree([2, 2, 2, 3, None, 3, None])
        expected = [[2, 3], [3]]
        result = self.solution.findDuplicateSubtrees(root)
        result_list = [self.binary_tree_to_list(node) for node in result]
        self.assertEqual(sorted(result_list), sorted(expected))


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        res = []
        subtrees = defaultdict(list)

        def dfs(node):
            if not node:
                return "N"
            s = str(node.val) + "," + dfs(node.left) + "," + dfs(node.right)
            if len(subtrees[s]) == 1:
                res.append(node)
            subtrees[s].append(node)
            return s

        dfs(root)
        return res


if __name__ == "__main__":
    unittest.main()
