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

    def binary_tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
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

    def list_to_binary_tree(self, lst):
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

    def test_evaluateTree_example1(self):
        root = self.list_to_binary_tree([2, 1, 3, None, None, 0, 1])
        self.assertTrue(self.solution.evaluateTree(root))

    def test_evaluateTree_example2(self):
        root = self.list_to_binary_tree([0])
        self.assertFalse(self.solution.evaluateTree(root))


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node.left and not node.right:
                return True if node.val == 1 else False
            if node.val == 2:
                return dfs(node.left) or dfs(node.right)
            else:
                return dfs(node.left) and dfs(node.right)

        return dfs(root)


if __name__ == "__main__":
    unittest.main()
