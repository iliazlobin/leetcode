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

    def binary_tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
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

    def test_tree2str_example1(self):
        root = self.list_to_binary_tree([1, 2, 3, 4])
        expected = "1(2(4))(3)"
        result = self.solution.tree2str(root)
        self.assertEqual(result, expected)

    def test_tree2str_example2(self):
        root = self.list_to_binary_tree([1, 2, 3, None, 4])
        expected = "1(2()(4))(3)"
        result = self.solution.tree2str(root)
        self.assertEqual(result, expected)


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                return ""
            left = dfs(node.left)
            right = dfs(node.right)
            r = str(node.val)
            if left and right:
                r += "(" + left + ")(" + right + ")"
            elif not left and right:
                r += "()(" + right + ")"
            elif left and not right:
                r += "(" + left + ")"
            return r

        return dfs(root)


if __name__ == "__main__":
    unittest.main()
