import sys
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

    def test_isValidBST(self):
        root = list_to_binary_tree([2, 1, 3])
        result = self.solution.isValidBST(root)
        self.assertEqual(result, True)

        root = list_to_binary_tree([1, 2, 3])
        result = self.solution.isValidBST(root)
        self.assertEqual(result, False)

        root = list_to_binary_tree([5, 4, 6, None, None, 3, 7])
        result = self.solution.isValidBST(root)
        self.assertEqual(result, False)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dps(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False
            if not (
                dps(node.left, left, node.val) and dps(node.right, node.val, right)
            ):
                return False
            return True

        return dps(root, -sys.maxsize - 1, sys.maxsize)


if __name__ == "__main__":
    unittest.main()
