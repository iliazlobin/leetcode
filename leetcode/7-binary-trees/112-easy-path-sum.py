import unittest
from collections import Counter
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(
            root.right, targetSum
        )


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

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

    def test_hasPathSum_example1(self):
        root = self.list_to_binary_tree(
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
        )
        targetSum = 22
        self.assertTrue(self.solution.hasPathSum(root, targetSum))

    def test_hasPathSum_example2(self):
        root = self.list_to_binary_tree([1, 2, 3])
        targetSum = 5
        self.assertFalse(self.solution.hasPathSum(root, targetSum))

    def test_hasPathSum_example3(self):
        root = self.list_to_binary_tree([])
        targetSum = 0
        self.assertFalse(self.solution.hasPathSum(root, targetSum))

    def test_hasPathSum_specific_case(self):
        root = self.list_to_binary_tree([1, 2])
        targetSum = 1
        self.assertFalse(self.solution.hasPathSum(root, targetSum))


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, total, isLeaf):
            if not node:
                return isLeaf and total == targetSum
            if dfs(node.left, total + node.val, not node.right) or dfs(
                node.right, total + node.val, not node.left
            ):
                return True

        if not root:
            return False
        return dfs(root, 0, not root.left and not root.right)


if __name__ == "__main__":
    unittest.main()
