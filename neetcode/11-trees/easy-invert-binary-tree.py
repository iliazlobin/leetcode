import unittest
from collections import Counter
from typing import List, Optional

from torch import inverse


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

    def test_invertTree(self):
        root = list_to_binary_tree([1, 2, 3, 4, 5, 6, 7])
        result = self.solution.invertTree(root)
        self.assertEqual(binary_tree_to_list(result), [1, 3, 2, 7, 6, 5, 4])

        root = list_to_binary_tree([3, 2, 1])
        result = self.solution.invertTree(root)
        self.assertEqual(binary_tree_to_list(result), [3, 1, 2])

        root = list_to_binary_tree([])
        result = self.solution.invertTree(root)
        self.assertEqual(binary_tree_to_list(result), [])


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        return root


if __name__ == "__main__":
    unittest.main()
