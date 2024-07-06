import unittest
from collections import Counter, deque
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

    def test_flatten_example1(self):
        root = list_to_binary_tree([1, 2, 5, 3, 4, None, 6])
        self.solution.flatten(root)
        expected_output = [1, None, 2, None, 3, None, 4, None, 5, None, 6]
        res = binary_tree_to_list(root)
        self.assertEqual(res, expected_output)

    def test_flatten_example2(self):
        root = list_to_binary_tree([])
        self.solution.flatten(root)
        expected_output = []
        self.assertEqual(binary_tree_to_list(root), expected_output)

    def test_flatten_example3(self):
        root = list_to_binary_tree([0])
        self.solution.flatten(root)
        expected_output = [0]
        self.assertEqual(binary_tree_to_list(root), expected_output)


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        return None

if __name__ == "__main__":
    unittest.main()
