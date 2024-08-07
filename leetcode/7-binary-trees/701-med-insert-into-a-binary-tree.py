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

    def test_insertIntoBST_example1(self):
        root = self.list_to_binary_tree([4, 2, 7, 1, 3])
        val = 5
        expected = [4, 2, 7, 1, 3, 5]
        result = self.solution.insertIntoBST(root, val)
        self.assertEqual(self.binary_tree_to_list(result), expected)

    def test_insertIntoBST_example2(self):
        root = self.list_to_binary_tree([40, 20, 60, 10, 30, 50, 70])
        val = 25
        expected = [40, 20, 60, 10, 30, 50, 70, None, None, 25]
        result = self.solution.insertIntoBST(root, val)
        self.assertEqual(self.binary_tree_to_list(result), expected)

    def test_insertIntoBST_example3(self):
        root = self.list_to_binary_tree(
            [4, 2, 7, 1, 3, None, None, None, None, None, None]
        )
        val = 5
        expected = [4, 2, 7, 1, 3, 5]
        result = self.solution.insertIntoBST(root, val)
        self.assertEqual(self.binary_tree_to_list(result), expected)


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        return root


if __name__ == "__main__":
    unittest.main()
