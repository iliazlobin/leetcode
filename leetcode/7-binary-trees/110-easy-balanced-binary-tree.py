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

    def test_isBalanced(self):
        # Example test case
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)

        self.assertFalse(self.solution.isBalanced(root))

    def test_isBalanced_balanced(self):
        # Balanced tree test case
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        self.assertTrue(self.solution.isBalanced(root))


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (0, True)

            leftD, leftB = dfs(node.left)
            if not leftB:
                return (0, False)
            rightD, rightB = dfs(node.right)
            if not rightB:
                return (0, False)

            return (max(leftD, rightD) + 1, abs(leftD - rightD) <= 1)

        _, balanced = dfs(root)
        return balanced


if __name__ == "__main__":
    unittest.main()
