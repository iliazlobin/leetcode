import unittest
from collections import Counter
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_binary_tree(lst: List[int]) -> Optional[TreeNode]:
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        node = queue.pop(0)
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root


def binary_tree_to_list(root: Optional[TreeNode]) -> List[int]:
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
    return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxPathSum(self):
        # Example 1
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        self.assertEqual(self.solution.maxPathSum(root1), 6, "Example 1 failed")

        # Example 2
        root2 = TreeNode(-10)
        root2.left = TreeNode(9)
        root2.right = TreeNode(20)
        root2.right.left = TreeNode(15)
        root2.right.right = TreeNode(7)
        self.assertEqual(self.solution.maxPathSum(root2), 42, "Example 2 failed")


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum = float("-inf")

        def dfs(node):
            nonlocal maximum

            if not node:
                return 0

            maxLeft = dfs(node.left)
            maxRight = dfs(node.right)
            maximum = max(maximum, maxLeft + maxRight + node.val)
            return max(maxLeft + node.val, maxRight + node.val, node.val, 0)

        dfs(root)
        return maximum


if __name__ == "__main__":
    unittest.main()
