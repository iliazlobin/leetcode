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

    def find_node(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        left = self.find_node(root.left, val)
        if left:
            return left
        return self.find_node(root.right, val)

    def test_lowestCommonAncestor_example1(self):
        root = self.list_to_binary_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = self.find_node(root, 2)
        q = self.find_node(root, 8)
        expected = 6
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, expected)

    def test_lowestCommonAncestor_example2(self):
        root = self.list_to_binary_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = self.find_node(root, 2)
        q = self.find_node(root, 4)
        expected = 2
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, expected)

    def test_lowestCommonAncestor_example3(self):
        root = self.list_to_binary_tree([2, 1])
        p = self.find_node(root, 2)
        q = self.find_node(root, 1)
        expected = 2
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, expected)


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                break
        return cur


if __name__ == "__main__":
    unittest.main()
