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

    def test_invertTree_example1(self):
        root = list_to_binary_tree([4, 2, 7, 1, 3, 6, 9])
        inverted_root = self.solution.invertTree(root)
        self.assertEqual(binary_tree_to_list(inverted_root), [4, 7, 2, 9, 6, 3, 1])

    def test_invertTree_example2(self):
        root = list_to_binary_tree([2, 1, 3])
        inverted_root = self.solution.invertTree(root)
        self.assertEqual(binary_tree_to_list(inverted_root), [2, 3, 1])

    def test_invertTree_example3(self):
        root = list_to_binary_tree([])
        inverted_root = self.solution.invertTree(root)
        self.assertEqual(binary_tree_to_list(inverted_root), [])


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None

            node.right, node.left = dfs(node.left), dfs(node.right)
            return node

        return dfs(root)


if __name__ == "__main__":
    unittest.main()
