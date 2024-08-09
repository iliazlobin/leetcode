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

    def test_deleteNode_example1(self):
        root = self.list_to_binary_tree([5, 3, 6, 2, 4, None, 7])
        key = 3
        expected = [5, 4, 6, 2, None, None, 7]
        result = self.solution.deleteNode(root, key)
        self.assertEqual(self.binary_tree_to_list(result), expected)

    def test_deleteNode_example2(self):
        root = self.list_to_binary_tree([5, 3, 6, 2, 4, None, 7])
        key = 0
        expected = [5, 3, 6, 2, 4, None, 7]
        result = self.solution.deleteNode(root, key)
        self.assertEqual(self.binary_tree_to_list(result), expected)

    def test_deleteNode_example3(self):
        root = self.list_to_binary_tree([])
        key = 0
        expected = []
        result = self.solution.deleteNode(root, key)
        self.assertEqual(self.binary_tree_to_list(result), expected)


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, cur.val)

        return root


if __name__ == "__main__":
    unittest.main()
