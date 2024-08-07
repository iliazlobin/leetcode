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

    def test_isSubtree_example1(self):
        root = list_to_binary_tree([3, 4, 5, 1, 2])
        subRoot = list_to_binary_tree([4, 1, 2])
        self.assertTrue(self.solution.isSubtree(root, subRoot))

    def test_isSubtree_example2(self):
        root = list_to_binary_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
        subRoot = list_to_binary_tree([4, 1, 2])
        self.assertFalse(self.solution.isSubtree(root, subRoot))

    def test_isSubtree_empty_subtree(self):
        root = list_to_binary_tree([1, 2, 3])
        subRoot = list_to_binary_tree([])
        self.assertTrue(self.solution.isSubtree(root, subRoot))

    def test_isSubtree_empty_tree(self):
        root = list_to_binary_tree([])
        subRoot = list_to_binary_tree([1])
        self.assertFalse(self.solution.isSubtree(root, subRoot))

    def test_isSubtree_both_empty(self):
        root = list_to_binary_tree([])
        subRoot = list_to_binary_tree([])
        self.assertTrue(self.solution.isSubtree(root, subRoot))


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return same(node1.left, node2.left) and same(node1.right, node2.right)

        def dfs(node):
            if not node:
                return False
            if same(node.left, subRoot) or same(node.right, subRoot):
                return True
            if dfs(node.left) or dfs(node.right):
                return True

        return same(root, subRoot) or dfs(root)


if __name__ == "__main__":
    unittest.main()
